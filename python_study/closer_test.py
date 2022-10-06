def logger(msg):
    def log_message():
        print('Log: ',msg)
    
    return log_message

log_hi = logger('Hi')       
# msg로 'Hi'가 전달, log_hi에 log_message 함수가 저장
# Hi는 logger함수로 전달된 지역함수이지만, 함수가 종류되어도 Hi를 기억할 수 있다.
print(log_hi)