# Merge Sort

def merges(lst):
    if len(lst)>1:

        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        merges(left)
        merges(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i]<right[j]:
                lst[k]= left[i]
                i=i+1
            else:
                lst[k]=right[j]
                j=j+1
            
            k=k+1
        
        while i < len(left):
            lst[k]=left[i]
            i =i+1
            k =k+1

        while j < len(right):
            lst[k]=right[j]
            j =j+1
            k =k+1

lst =  [2,9,6,1,0,5,7,3]
merges(lst)
print(lst)

