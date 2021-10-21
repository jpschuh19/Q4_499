import sys

def print_to_stdout(a):
    print(a, file=sys.stdout)

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    with open(line) as f:
        names = f.readlines()

names.sort()
names.sort(key=len, reverse=True)

def print_forward():
    for i in names:
        print_to_stdout(names[i])

def print_reverse():
    i=len(names)-1
    while(i>=0):
        print_to_stdout(names[i])
        i+=1

