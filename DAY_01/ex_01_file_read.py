#------------------------------------------
# 파일 입출력 => 출력 즉, 읽기(read)
# - 사용 내장 함수 : open(file, mode='rt[기본값]', encoding='시스템 기본값')
# - encoding 설정 : 파일에 적용된 인코딩을 설정해야 함!
#------------------------------------------
#(1) open
file=open('message.txt', encoding='utf8')

print(f'file => {type(file)}, {file}') # 파일명과, 파일내용, 파일 인코딩에 대한 전체의 내용이 file에 들어간다

#(2) IO => read() : 파일 안에 모든 내용 다 읽어오기
fdata=file.read()
print(fdata)

#(2) IO => read(n) : 지정된 숫자만큼 문자를 파일에서 읽어오기
fdata=file.read(5) # 이미 read로 다 읽어들였기 때문에 다시 읽어도 값이 없음
                   #위에 read를 주석하고 실행하면 다섯 글자만 읽어오는 것을 알 수 있다(5 bytes)
print(fdata)
fdata=file.read(5)
print(fdata)       # " new "가 나왔음을 알 수 있다.(양옆 공백도 포함)
#(2) IO => readline() : "\n"기준으로 한 줄 읽어오기
while True :
    fline=file.readline()
    if not fline:
        break
    print(f'fline => {type(fline)},{fline}', end="")



fline=file.readlines() # 한 줄씩 읽어오는 메서드
print(f'fline => {type(fline)},{fline}', end="")
# (3) close
file.close()