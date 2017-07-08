def CFchange(F):
	C = (F-32)*5/9
	return C

if __name__ == '__main__':
	C = CFchange(int(input()))
	print(C)