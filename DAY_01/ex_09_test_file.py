#----------------------------------------------------------
# 입력받은 내용을 파일에 저장하는 프로그램
# - 조건 : 'X', 'x' 입력 시 입력받기 중단
#----------------------------------------------------------
from time import *
from datetime import date, datetime
today=date.today()
print(today.year, today.month, today.day)
today2=datetime.today()
print(today2.year, today2.month, today2.day, today2.hour, today2.minute, today2.second, today2.microsecond)

print(ctime(time())) # 현재 시간을 출력해준다
print(localtime(time()))
print(today.strftime('%d/%m/%y'))
print(today.strftime('%y/%m,%d'))
# 관련 변수 ------------------------------------------------
filename="test.txt"


# 프로그램 기능 구현 부분 -------------------------------------
with open(filename,mode='a',encoding='utf8') as f : # 컴퓨터 입장에서는 한번 열어놓고 하는게 편하다
    while True:
        data=input("메시지 입력 (종료-X,x) : ")
        # 종료 검사
        if data.upper() =="X" :
            print("종료합니다.")
            # 종료 전에 파일에 기록
            break # 즉시 종료로 while문에서 아래 코드 실행 안됌

        # 파일에 쓰기 즉 저장
        f.write(f'{ctime(time())} : {data}\n')
        # 일정 시간 일시정지 후 반복하기
        sleep(1)

    f.write(f'저장시간 : {ctime(time())}\n')



