import time
with open('test.txt', "r+") as fi:
    data = fi.read()
start = int(data)
i=start/50+1
s=start%50
print(s)
print(int(i))
start = start + 1
with open('test.txt','w') as fi:
	fi.write(str(start))
