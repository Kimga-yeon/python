#!/Users/gayun3_3/AppData/Local/Programs/Python/Python38-32/pythonw.exe
print("Content-Type: text/html")
print()

#한글로 작성시 포함해야 에러안남
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#-----

print('''<!doctype html>
<html>
<head>
  <title> welcome </title>
  <meta charset="utf-8">

</head>
<body>
  <h1>다같이 이겨내요</h1>
<ol>
  <li>신종 코로나란?</li>
  <li>국민안심병원</li>
  <li>지원현황</li>
</ol>
<H2><font color="brik">"코로나는 코리아를 이길 수 없습니다."</font></H2>
<P>유명 카피라이터 정철이 신종 코로나바이러스 감염증(코로나19) 확산을 막기 위해 펼치는
  캠페인 '고마워요, 질병관리본부'가 눈길을 끌고 있다. #고맙습니다 #응원합니다 #힘내십시오 #함께하겠습니다
</P>
</body>
</html>
''')
