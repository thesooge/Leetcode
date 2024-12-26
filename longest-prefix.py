
ini_strlist = ['akshat', 'akash', 'akshay', 'akshita']

# Finding common prefix using Naive Approach
res = ''
prefix = ini_strlist[0]

for string in ini_strlist[1:]:
	while string[:len(prefix)] != prefix:
		prefix = prefix[:len(prefix)-1]
res = prefix

# Printing result
print("Resultant prefix", str(res))
