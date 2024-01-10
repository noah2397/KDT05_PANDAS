#------------------------------------------
# 파일을 하나 선택 후 복사본 파일 생성하기
# - 예) message.txt ===> messsage_copy.txt
#------------------------------------------


filename='message.txt'
with open(filename, "r", encoding="utf-8") as origin: # 기존의 파일을 읽기 모드로 열기
    with open(f'{filename[:filename.index(".txt")]}_copy.txt', "w", encoding="utf-8") as copy:
        '''
        복사할 파일을 쓰기 모드로 연 뒤에, 기존 파일 뒤에 _copy.txt가 붙도록 인덱스로 설정
        '''
        copy.write(origin.read()) # read로 기존 파일의 내용을 다 읽은 걸 카피본에 다 처넣음

