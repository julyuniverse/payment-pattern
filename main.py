import pandas as pd  # 데이터를 저장하고 처리하는 패키지
import matplotlib.pyplot as plt  # 그래프를 그리는 패키지
import numpy as np  # 벡터, 행렬 등 수치 연산을 수행하는 선형대수(Linear algebra) 라이브러리

# 한글 깨짐 방지
plt.rc('font', family='Malgun Gothic')

# csv 파일 읽어 오기
df = pd.read_csv('어린이날_결제_기존_고객_1년간_출석_일수.csv')

# 고객별 출석 일수
plt.plot(df.rownum, df.attendance_count, color='green', linestyle='solid', label='출석 일수')

# 출석 평균
attendance_count_mean = [df.attendance_count.mean()] * len(df.rownum)
plt.plot(df.rownum, attendance_count_mean, color='blue', linestyle='solid', label='평균')

# y축 눈금 출력 단위 설정
plt.yticks(np.arange(0, df.attendance_count.max(), 5))

# 제목
plt.title("어린이날 결제 기존 고객 1년간 출석 일수")

# 그리드
plt.grid(True)

# y축에 레이블 추가하기
plt.ylabel("출석 일수")
plt.xlabel("고객 수")

# 범례
plt.legend(loc=0)

# 그래프 출력
plt.show()
