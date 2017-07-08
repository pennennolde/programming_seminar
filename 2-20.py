import sys

def lower(cap):
	small = cap + 32
	return small

# line = list(sys.stdin.read())
line = list(sys.stdin)
print(line)

for char in line:
	code = ord(char)
	if code>=65 and code<=90: # 大文字
		code = lower(code)
	print(chr(code), end="")


# 標準入力
# エンターを押していくことで何行でも入力できる
# 入力を終えるときは　ctrl z で終われる

# sys.stdin.read()  → 1文字ずつ全部読み込む
# sys.stdin.read(1)  → 1文字だけ読み込む
# sys.stdin         → 1単語ずつ全部読み込む





# import sys

# def lower(cap):
# 	small = cap + 32
# 	return small


# line = list(input())


# #for char in sys.stdin.read(1):
# for char in line:

# 	code = ord(char)
# 	if code>=65 and code<=90: # 大文字
# 		code = lower(code)
# 	print(chr(code), end="")
