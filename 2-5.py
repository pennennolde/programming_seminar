import sys

def any(s1, s2):
	s1 = list(s1)
	s2 = list(s2)
	index = 0
	for char1 in s1:
		for char2 in s2:
			if char1==char2:
				return index
		index += 1
		if index==len(s1)-1:	# 改行文字は検査しないように
			return -1


print("もとの文字列 s1 を入力してください。")
s1 = sys.stdin.readline()

print("次に文字列 s2 を入力してください。")
s2 = sys.stdin.readline()

index = any(s1, s2)
if index!=-1:
	print("s2の中のいずれかの文字が、s1の中で最初に出てくるのは、s1の", index+1, "文字目で、", s1[index], "です。")
else:
	print("s2の中のどの文字も、s1の中に存在しません。")