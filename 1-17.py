import sys

def getline():
	line = sys.stdin.readline()
	return line

while getline():
	if len(getline()) > 80:
		print(getline())




# 関数定義 def →　　()　をつける必要がある