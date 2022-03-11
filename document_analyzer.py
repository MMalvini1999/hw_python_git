def counter():
	with  open('document.txt') as f:
		contents = f.read()
		print(contents)	
	contents.split()
	splitting=contents.split()
	print(splitting)
	i=0
	while i<5:
		print("word: ")
		i=i+1
	f.close()
	return contents

counter()
