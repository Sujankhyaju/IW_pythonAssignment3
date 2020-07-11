# Bubble Sort


def bubble(lst):

    for i in range(len(lst)-1):
        if lst[i]> lst[i+1]:
            temp = lst[i]
            lst[i]= lst[i+1]
            lst[i+1] = temp


lst = [2,9,6,1,0,5,7,3]

for _ in range(len(lst)-1):
    bubble(lst)

print(lst)
