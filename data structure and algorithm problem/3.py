# Quick Sort

def quick(lst,first,last):
    if first < last:
        split_index = partition(lst,first,last)
        print(split_index)

        quick(lst,first,split_index-1)
        quick(lst,split_index+1,last)

def partition(lst,first,last):
    
    pivot = lst[last]
    index = first - 1

    for i in range(first,last):
        if lst[i] <= pivot:
            index = index + 1
            lst[index] = lst[i]
            lst[i]=lst[index]

    lst[index + 1]= lst[last]
    lst[last] = lst[index + 1]

    return index + 1


lst = [2,9,6,1,0,5,7,3]
quick(lst,0,len(lst)-1)
print(lst)


