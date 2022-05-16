import pandas as pd  # 데이터를 저장하고 처리하는 패키지
import matplotlib.pyplot as plt  # 그래프를 그리는 패키지
import numpy as np  # 벡터, 행렬 등 수치 연산을 수행하는 선형대수(Linear algebra) 라이브러리


# 레이블 값 추가
def add_value_label(x_list, y_list):
    for i in range(1, len(x_list) + 1):
        plt.text(i - 1, y_list[i - 1], y_list[i - 1], ha="center")


# 한글 깨짐 방지
plt.rc('font', family='Malgun Gothic')

# csv 파일 읽어 오기
df = pd.read_csv('어린이날_결제_기존_고객_1년간_학습_모드.csv')

# 학습 모드 개수
plt.bar(df.learning_mode, df.learning_mode_count, color='green', linestyle='solid', label='학습 모드별 개수')

# 학습 모드 %
a = np.array(df.learning_mode_count)
for i in range(0, len(df.learning_mode)):
    a[i] = a[i] / sum(df.learning_mode_count) * 100
add_value_label(df.learning_mode, a)
plt.plot(df.learning_mode, a, color='skyblue', linestyle='solid', label='학습 모드별 %')

# y축 눈금 출력 단위 설정
plt.yticks(np.arange(0, df.learning_mode_count.max(), 50))

# add_value_label
add_value_label(df.learning_mode, df.learning_mode_count)

# 제목
plt.title("어린이날 결제 기존 고객 1년간 학습 모드별 개수")

# y축에 레이블 추가하기
plt.ylabel("학습 모드별 개수")
plt.xlabel("학습 모드")

# 범례
plt.legend(loc=0)

# 그래프 출력
plt.show()
