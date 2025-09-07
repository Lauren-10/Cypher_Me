
def hand_value(hand_str):
	vals = sorted("23456789TJQKA".index(i) for i in hand_str[::3])
	unique_ranks = len(set(vals))
	if unique_ranks == 5:  # straight, flush, straight flush, or high card
		is_straight = vals[0] + 4 == vals[4]
		is_flush = len(set(hand_str[1::3])) == 1
		if is_straight and is_flush:
			return 8 * 13**5 + vals[4]
		elif is_straight:
			return 4 * 13**5 + vals[4]
		elif is_flush:
			return 5 * 13**5 + sum(vals[i] * 13**i for i in range(5))
		else:
			return sum(vals[i] * 13**i for i in range(5))
	elif unique_ranks == 4:  # one pair
		if vals[0] == vals[1]:
			p, c0, c1, c2 = vals[0], vals[2], vals[3], vals[4]
		elif vals[1] == vals[2]:
			p, c0, c1, c2 = vals[1], vals[0], vals[3], vals[4]
		elif vals[2] == vals[3]:
			p, c0, c1, c2 = vals[2], vals[0], vals[1], vals[4]
		else:
			p, c0, c1, c2 = vals[3], vals[0], vals[1], vals[2]
		return 1 * 13**5 + p * 13**3 + c2 * 13**2 + c1 * 13 + c0
	elif unique_ranks == 3:  # two pairs or three of a kind
		if vals[0] == vals[2] or vals[1] == vals[3] or vals[2] == vals[4]:
			if vals[0] == vals[2]:
				t, c0, c1 = vals[0], vals[3], vals[4]
			elif vals[1] == vals[3]:
				t, c0, c1 = vals[1], vals[0], vals[4]
			else:
				t, c0, c1 = vals[2], vals[0], vals[1]
			return 3 * 13**5 + t * 13**2 + c1 * 13 + c0
		else:
			if vals[0] != vals[1]:
				p0, p1, c = vals[1], vals[3], vals[0]
			elif vals[2] != vals[3]:
				p0, p1, c = vals[0], vals[3], vals[2]
			else:
				p0, p1, c = vals[0], vals[2], vals[4]
			return 2 * 13**5 + p1 * 13**2 + p0 * 13 + c
	else:  # four of a kind or full house
		if vals[0] == vals[3] or vals[1] == vals[4]:
			if vals[0] == vals[3]:
				q, c = vals[0], vals[4]
			else:
				q, c = vals[1], vals[0]
			return 7 * 13**5 + q * 13 + c
		else:
			if vals[0] == vals[2]:
				t, p = vals[0], vals[3]
			else:
				t, p = vals[2], vals[0]
			return 6 * 13**5 + t * 13 + p

def p54():
    lines = []
    file = open('codeforces/poker.txt', 'r')
    lines = file.readlines()
    res = 0
    for line in lines:
        hand1_str = line[0:14]
        hand2_str = line[15:29]
        if hand_value(hand1_str) > hand_value(hand2_str):
            res += 1
    
    return res

print(p54())