h_count=0
sort_count=0
def h_part(A,p,r):
    print(A,p,r)
    global h_count
    h_count+=1
    x=A[p]
    i=p-1
    j=r+1

    while (1):
        while (1):
            j-=1
            if A[j]<=x:
                break
        while(1):
            i+=1
            if A[i]>=x:
                break
        if i<j:
            A[i],A[j]=A[j],A[i]
        else:
            ##A[p],A[j]=A[j],A[p]
            print(A)
            print("pivot=",j)
            print("--------------------------")
            return j
      
def sort(A,p,r):
    global sort_count
    sort_count+=1
    if p<r:
        q=h_part(A,p,r)
        sort(A,p,q-1)
        sort(A,q+1,r)


list=[13,19,9,5,12,8,7,4,11,2,6,21,30]
sort(list,0,len(list)-1)
print(h_count)
print(sort_count)
"""
def h_part(A,p,r):
    x=A[p]
    i=p-1
    j=r+1

    while (1):
        while (1):
            j-=1
            if A[j]<=x:
                break
        while(1):
            i+=1
            if A[i]>=x:
                break
        if i<j:
            A[i],A[j]=A[j],A[i]
        else:
            print(A)
            print(j)
            return j
            """   