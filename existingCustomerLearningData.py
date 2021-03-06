import pandas as pd  # 데이터를 저장하고 처리하는 패키지
import matplotlib.pyplot as plt  # 그래프를 그리는 패키지
import numpy as np  # 벡터, 행렬 등 수치 연산을 수행하는 선형대수(Linear algebra) 라이브러리


# 레이블 값 추가
def add_value_label(x_list, y_list):
    for i in range(1, len(x_list) + 1):
        plt.text(i, y_list[i - 1], y_list[i - 1], ha="center")


# 한글 깨짐 방지
plt.rc('font', family='Malgun Gothic')

# csv 파일 읽어 오기
df = pd.read_csv('어린이날_결제_기존_고객_1년간_학습_데이터.csv')

# 고객별 학습 개수
plt.plot(df.rownum, df.learning_data_count, color='green', linestyle='solid', label='학습 개수')

# 학습 개수 평균
learning_data_count_mean = [df.learning_data_count.mean()] * len(df.rownum)
plt.plot(df.rownum, learning_data_count_mean, color='blue', linestyle='solid', label='평균')

# 학습 개수 중앙값
learning_data_count_median = [df.learning_data_count.median()] * len(df.rownum)
plt.plot(df.rownum, learning_data_count_median, color='skyblue', linestyle='solid', label='중앙값')

# x축 눈금 출력 단위 설정
plt.xticks(np.arange(0, df.rownum.max(), 1))

# y축 눈금 출력 단위 설정
plt.yticks(np.arange(0, df.learning_data_count.max(), 5))

# Float to Int
a = np.array(learning_data_count_mean, dtype=int)
add_value_label(df.rownum, a)
a2 = np.array(learning_data_count_median, dtype=int)
add_value_label(df.rownum, a2)

# 제목
plt.title("어린이날 결제 기존 고객 1년간 학습 데이터")

# 그리드
plt.grid(True)

# y축에 레이블 추가하기
plt.ylabel("학습 개수")
plt.xlabel("고객 수")

# 범례
plt.legend(loc=0)

# 그래프 출력
plt.show()
