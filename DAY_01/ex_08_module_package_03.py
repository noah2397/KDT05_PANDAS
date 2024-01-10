#-------------------------------------------------------
# 패키지 사용법
#  => import뒤에 패키지가 오지 않도록 한다
#     import 패키지.모듈이름
#     from 패키지 import 모듈이름
#_------------------------------------------------------
# 사용할 모듈 로딩 ---------------------------------------
#import urllib
#urllib.request.urlopen() # 점을 찍었는데 안나온다 -> urllib가 패키지이기 때문

# 따라서 다음과 같이 쳐야한다
import urllib.request as req# import뒤에 패키지 이름이 아닌 모듈이 오도록 코딩을 해야한다
from urllib import request, error
from http.client import HTTPResponse # urlopen을 한 뒤 반환하는 responsible객체를 나타내는 값 import

# from 패키지명 import 모듈명
dataObj=req.urlopen("https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
print(dataObj)