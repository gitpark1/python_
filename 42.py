def solution(a, b):
    month_day=[31,29,31,30,31,30,31,31,30,31,30]
    days=["SUN","MON","TUE","WED","THU","FRI","SAT"]
    
    t=0
    
    for i in range(a-1):
        t+=month_day[i]
        
    day_i=(t+b-1)%7
    
    return days[(5+day_i)%7]
    