import queue
import numpy as np
def p39(cap=1000):
	q = queue.SimpleQueue()
	q.put_nowait(np.array([3,4,5]))
	A = np.array([[1,-2,2],[2,-1,2],[2,-2,3]])
	B = np.array([[1,2,2],[2,1,2],[2,2,3]])
	C = np.array([[-1,2,2],[-2,1,2],[-2,2,3]])
	perims = [0 for _ in range(cap+1)]
	while not q.empty():
		v = q.get_nowait()
		for child in [A @ v, B @ v, C @ v]:
			if sum(child) <= cap:
				q.put_nowait(child)
		p = sum(v)
		for mult in range(p, cap+1, p):
			perims[mult] += 1
	return perims.index(max(perims))

print(p39())