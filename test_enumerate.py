list=["test","one"]

for i, j in enumerate(list):
	print(i,j)


for i in enumerate(list):
	print(i)

for j in enumerate(list):
	print(j[0])
	print(j[1])
