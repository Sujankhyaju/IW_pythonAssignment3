# Linear Search

def linearSearch(lst,item):

    index = 0
    flag = False
    while index < len(lst) and not flag:
        if lst[index] == item:
            flag = True
        else:
            index +=1 

    return item,flag,index


lst = [2,9,6,1,0,5,7,3]
item = 0
print(linearSearch(lst,item))
