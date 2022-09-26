def solution(arr1, arr2):
    answer = []
    in_list=[]
    for i,b in zip(arr1,arr2):
        in_list=[]
        for a in range(len(i)):
            
            in_list.append(i[a]+b[a])
        answer.append(in_list)
    return answer

arr1=[[1,2,3,4],[4,5,6,7],[1,2,3,3]]
arr2= [[3, 2, 1, 5], [6, 5, 4, 9], [4, 5, 6, 7]]
a=solution(arr1,arr2)
print (a)