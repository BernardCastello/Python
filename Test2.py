x = "C\Users\bernard.castello\Documents\classMates.txt"
y = raw_input ("Type in a name")

def open(Path, x):
	with open(Path) as file:
		for line in file:
			if y in file:
		print (line)
			break:
		else:
			print("Searching...")
	print("Name not found")
			
'''def splitFile(Path, x):
	first = []:
	last = []:
	z = :
	with open(Path, y):'''