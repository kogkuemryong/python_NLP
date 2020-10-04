# 레빈슈타인 거리
def dtance_lvenshtein(text1, text2):
    if text1 == text2: return "차이가 없다."

    text1_len = len(text1)
    text2_len = len(text2)

    if text1 == "": return text2_len
    if text2 == "": return text1_len

    matrix = [[] for i in range(text1_len + 1)]

    for i in range(text1_len + 1):
        matrix[i] = [0 for j in range(text2_len + 1)]
    for i in range(text1_len + 1):
        matrix[i][0] = i
    for i in range(text2_len + 1):
        matrix[0][i] = i
    for i in range(1, text1_len + 1):
        text1_calc = text1[i - 1]  # 계산 값은 거리에 값에서 하나씩 빼준값
        for j in range(1, text2_len + 1):
            text2_calc = text2[j - 1]  # 계산 값은 거리에 값에서 하나씩 빼준값
            total_calc = 0 if (text1_calc == text2_calc) else 1
            matrix[i][j] = min([matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + total_calc])
    return matrix[text1_len][text2_len]


text_list = ["강남역", "건대역", "강남대역", "홍대역", "화랑대역", "송파역","마포시장역"]

for i in text_list:
    print("거리 [" + text_list[0] + "] vs [" + str(i) + "]", dtance_lvenshtein("강남역",i) )