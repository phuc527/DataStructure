import time


def stack(st):
	mang = []
	while st != 0:
		a = st % 2
		mang.append(a)
		st = st // 2
	b = ''
	while mang != []:
		c = mang.pop()
		b += str(c)
	print(b)
st = int(input())


start = time.time()
stack(st)
end = time.time()
print(f"time: {end - start}")