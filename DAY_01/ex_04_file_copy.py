#------------------------------------------
# 파일을 하나 선택 후 복사본 파일 생성하기
# - 예) message.txt ===> messsage_copy.txt
#------------------------------------------


filename='message.txt'
with open(filename, "r", encoding="utf-8") as origin:
    with open(f'{filename[:filename.index(".txt")]}_copy.txt', "w", encoding="utf-8") as copy:
        copy.write(origin.read())
        