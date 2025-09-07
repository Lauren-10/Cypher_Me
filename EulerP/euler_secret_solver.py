import numpy as np

def fft_circ_conv2_mod(A: np.ndarray, B: np.ndarray, mod: int) -> np.ndarray:
    """Circular convolution of same-shaped 2D arrays A,B, modulo 'mod'."""
    H, W = A.shape
    FA = np.fft.rfftn(A, s=(H, W))
    FB = np.fft.rfftn(B, s=(H, W))
    FC = FA * FB
    C = np.fft.irfftn(FC, s=(H, W))
    return np.rint(C).astype(np.int64) % mod

def make_neighbor_kernel(shape):
    """Toroidal 4-neighbor kernel for given (H,W)."""
    H, W = shape
    K = np.zeros((H, W), dtype=np.int64)
    K[0, 1 % W] = 1
    K[0, (W - 1) % W] = 1
    K[1 % H, 0] = 1
    K[(H - 1) % H, 0] = 1
    return K

def pow_convolution_apply(image_mod: np.ndarray, kernel: np.ndarray, steps: int, mod: int) -> np.ndarray:
    """Compute (K^{(*steps)} * image) mod 'mod' using repeated squaring."""
    H, W = image_mod.shape
    assert kernel.shape == (H, W)

    # Precompute kernel powers
    powers = []
    Kpow = kernel.copy() % mod
    t = steps
    while t > 0:
        powers.append(Kpow)
        Kpow = fft_circ_conv2_mod(Kpow, Kpow, mod)
        t >>= 1

    # Apply per binary decomposition of steps
    result = image_mod.copy() % mod
    t = steps
    idx = 0
    while t > 0:
        if (t & 1) == 1:
            result = fft_circ_conv2_mod(result, powers[idx], mod)
        t >>= 1
        idx += 1
    return result % mod

if __name__ == "__main__":
    # Example hardcoded start array (replace with your own)
    arr = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 100],
        [66, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [65, 69, 0, 0, 0, 0, 0, 0, 0, 67],
        [68, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 98],
        [101, 0, 0, 0, 0, 0, 0, 0, 99, 97]
    ], dtype=np.int64)

    for i in arr:
        for j in i:
            j = j % 7

    mod = 7
    steps = 10**12   # smaller test run, can set to 10**12
    K = make_neighbor_kernel(arr.shape)

    result = pow_convolution_apply(arr % mod, K, steps, mod)
    summ = 0
    for i in range(6):
        for j in range(10):
            summ = summ + result[i][j]
        print(summ)
        summ = 0
    print(result)
