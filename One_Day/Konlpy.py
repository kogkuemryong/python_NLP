from konlpy.tag import Okt
# Okt : 트위터 분석기 - 트위터에서 한국어 처리 함

okt = Okt() # 객체 생성

text = okt.pos("태연은 노래를 잘 부릅니다.", norm= True , stem= True)

# print(text)

review = ["이 음식점의 고기는 질이 나빠요", "고기 맛은 모르겠는데, 직원들은 매우 친절합니다."]

for i in range(len(review)):
    text = okt.pos(review[i], norm=True, stem=True)
    print(text)