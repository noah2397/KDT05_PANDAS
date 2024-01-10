#------------------------------------------
# 파일 입출력 => 입력 즉, 쓰기(write)
# - 사용 내장 함수 : open(file, mode='w',encoding="지정값")
#------------------------------------------

filename=r'.\mydata.txt'
existfile=r'.\message.txt'
# (1) open => 쓰기(w) 모드의 경우 파일이 없으면 생성, 있으면 모든 내용 지움
#file=open(filename, mode='w', encoding='utf-8')


# (1) open => 쓰기(a : append) 모드의 경우 파일이 없으면 생성, 있으면 제일 마지막에 추가
file=open(filename,mode='a',encoding='utf-8')


# (2) write
# file.write("TEST\n") # 줄바꿈을 직접 지정해줘야한다
# file.write("Ha Ha Ha\n")
# file.write('''
#             Hahaha
#             assaaa
#             11111
#             ''') # 여러 줄 표현은 줄바꿈이 포함되어서 출력된다
file.writelines(['a\n','b\n','c\n'])

# (3) close
file.close()


