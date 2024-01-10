#----------------------------------------------------------
# 파일 데이터 접근 관련 메서드들
#----------------------------------------------------------
filename='message.txt'

with open(filename,mode='r',encoding='utf8') as f:
    f.seek(5)
    print(f.read(10))
    print(f.read(1))
    print(f'현재 위치 : {f.tell()}')
    f.seek(0)
    print(f'현재 위치 : {f.tell()}')

print(f.name, f.closed, f.mode) # 이미 닫혔을텐데 조회가 된다