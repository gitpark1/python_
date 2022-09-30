def solution(id_list, report, k):
    check={x:0 for x in id_list}
    
    for x in set(report):
        check[x.split()[1]]+=1
    
    report_list=[x[0] for x in check.items() if x[1]>=k]
    
    for x in check:
        check[x]=0
        
    for x in set(report):
        a=x.split()
        if a[1] in report_list:
            check[a[0]]+=1
    
    print(list(check.values()))
    return list(check.values())
    
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)