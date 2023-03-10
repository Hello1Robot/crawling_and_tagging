from konlpy.tag import Okt
okt = Okt()
text = '형태소분석을 테스트해보자'
tagging = okt.pos(text)
print(tagging)

from konlpy.tag import Kkma
kkma = Kkma()
tagging2 = kkma.pos(text)
print(tagging2)
