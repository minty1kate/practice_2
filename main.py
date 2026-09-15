def bruteforce(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		words = [line.strip() for line in f if line.strip()]

	max_len = 0
	answer = None

	for w1 in words:
		for w2 in words:
			if w1 == w2:
				continue

			for i in range(1, min(len(w1), len(w2)) + 1):
				suffix = w1[-i:]
				prefix = w2[:i]
				if suffix == prefix and i > max_len:
					max_len = i
					answer = (w1, w2)
					break

	return answer, max_len

def with_dict(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		words = [line.strip() for line in f if line.strip()]

	prefix_dict = {}
	for w in words:
		for i in range(1, len(w) + 1):
			prefix = w[:i]
			if prefix not in prefix_dict:
				prefix_dict[prefix] = []
			prefix_dict[prefix].append(w)

	max_len = 0
	answer = None

	for w1 in words:
		for i in range(1, len(w1) + 1):
			suffix = w1[-i:]
			if suffix in prefix_dict:
				for w2 in prefix_dict[suffix]:
					if w1 != w2 and i > max_len:
						max_len = i
						answer = (w1, w2)

	return answer, max_len