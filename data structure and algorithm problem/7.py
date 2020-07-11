# Interpolation Search

def interpolationSearch(lst,item):

    first = 0
    last = len(lst)-1
    flag = False

    while (first<last and not flag):
        mid = first + ((last-first)//(lst[last]-lst[first])) *(item - lst[first])
        
        if lst[mid] == item:
            flag = True

        else:
            if lst[mid]< item:
                first = mid +1
            
            else:
                last = mid -1
    return flag,mid

lst = [2,9,6,1,0,5,7,3]
lst = sorted(lst)
item  = 3
print(interpolationSearch(lst,item))



    