import sys

def expand(s):
	s = list(s)
	expanded_s = []
	index = 0
	for char in s:
		if char=="-":
			if index!=0 and index!=len(s)-2:
				start = int(ord(s[index-1])) + 1
				end = int(ord(s[index+1]))
				for num in range(start, end):
					expanded_s.append(chr(num))
			else:
				expanded_s.append("-")
		else:
			expanded_s.append(char)
		index += 1
	return expanded_s


s = sys.stdin.readline()
expanded_s = expand(s)

for char in expanded_s:
	print(char, end="")