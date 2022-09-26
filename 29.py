def solution(price, money, count):
    answer = -1
    total_price=count*(2*price+(count-1)*price)//2  #등차수열의 합 공식
    answer=0 if money>=total_price else total_price-money
    return answer