import sys
import random

#trivial change?

filename = sys.argv[1]
with open(filename) as file:
	for line in file:
		if random.random() < 0.01:
			sys.stdout.write(line)
