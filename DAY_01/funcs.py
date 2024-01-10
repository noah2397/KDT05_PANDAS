def add(x,y):
    return x+y
def div(x,y):
    return x/y

if __name__=='__main__': # 내가 import될 수 있으니까, import될 때는 실행되지 않도록 설정함
    print(f'funcs.py => __name__ : {__name__}')
    print(add(1,2))
    print(div(1,2))