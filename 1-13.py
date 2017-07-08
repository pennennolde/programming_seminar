import sys

words = list(sys.stdin.read().split())

histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for word in words:
	char_num = len(word)
	if char_num>=10:
		char_num = 10
	histogram[char_num-1] += 1


# printする
for i in range(10):
	if i+1<10:
		print(" ", i+1, ": ", end="")
	else:
		print(i+1, "=< ", end="")
	for j in range(histogram[i]):
		print("＊", end="")
	print()
