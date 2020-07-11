# Insertion Sort

def insertion(lst):
    
    for i in range(1,len(lst)):
        currentvalue = lst[i]
        index = i

        while index > 0 and lst[index-1]>currentvalue:
            lst[index] =lst[index-1] 
            index -= 1

        lst[index]= currentvalue

lst = [2,9,6,1,0,5,7,3]
insertion(lst)
print(lst)

        

        