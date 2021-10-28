import sys

def print_to_stdout(a):
    print(a, file=sys.stdout)

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    with open(line) as f:
        names = f.readlines()

forward_list = []
reverse_list = []

unsorted = names

names.sort()
names.sort(key=len, reverse=True)

def print_forward():
    for i in names:
        forward_list.append(names[i])
        print_to_stdout(names[i])

def print_reverse():
    i=len(names)-1
    while(i>=0):
        print_to_stdout(names[i])
        reverse_list.append(names[i])
        i+=1

def check_forward():
    x=0
    if(forward_list == unsorted):
        for i in forward_list:
            for j in unsorted:
                if(forward_list[i] != unsorted[j]):
                    print("Sorted list is NOT the same")
                    x=1
    else:
        print("Sorted list is NOT the same")
        x=1
    if(x==0):
        print("Sorted list is the same")

def check_reverse():
    x=0
    if(reverse_list == unsorted):
        for i in reverse_list:
            for j in unsorted:
                if (forward_list[i] != unsorted[j]):
                    print("Sorted list is NOT the same")
                    x=1
    else:
        print("Sorted list is NOT the same")
        x=1
    if(x==0):
        print("Sorted list is the same")

print_forward()
check_forward()


print_reverse()
check_reverse()
