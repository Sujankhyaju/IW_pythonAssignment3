# Binary Search

def binarySearch(lst,item):

    first = 0
    last = len(lst)-1
    flag = False

    while (first <=last and not flag):
        mid = (first + last)//2

        if lst[mid] == item:
            flag = True
            break
        else:
            if item < lst[mid]:
                last = mid -1
            
            else:
                first = mid +1

    return flag

lst = [2,9,6,1,0,5,7,3]
lst = sorted(lst)
item = 2
print(binarySearch(lst,item))
