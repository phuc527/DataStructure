import numpy.random as rd
import time
# print(st)

# def stack():
# 	st = list(rd.randint(100,size=20))
# 	m = st.pop()
# 	while(st!=[]):
# 		b = st.pop()
# 		if b > m:
# 			m = b
# 	print(st)
# 	print(m)

def stack():
	st = list(rd.randint(100,size=20))
	maxx = st[0]
	for i in range(len(st)):
		if maxx < st[i]:
			maxx = st[i]
	print(len(st))
	print(maxx)

start = time.time()
stack()
end = time.time()
print(f"Thoi gian chay: {end - start}")