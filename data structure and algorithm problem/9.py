# Tower of Hanoi problem for ‘n’ number of disks.

def TOH(n,source,desti,temp):
    if n==1:
        print(f"Move disk 1 from source {source} to destination {desti}.")
        return

    TOH(n-1,source,temp,desti)
    print(f"Move disk {n} from source {source} to destination {desti}.")
    TOH(n-1,temp,desti,source)

n=3
TOH(n,'A','B','C')
