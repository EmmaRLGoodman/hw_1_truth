import sys
import random

#adding things so things are different

filename = sys.argv[1]
writefile=open("samplit-emmagoodman.txt","a")
with open(filename) as file:
	for line in file:
		if random.random() < 0.01:
			writefile.write(line)
			sys.stdout.write(line)
