import pandas as pd

print(pd.__version__)

#   Series 클래스 < DataFrame 클래스
#   1차원 배열      2차원배열

s1 = pd.Series(
    [1,3,5], index=[10,20,30]       # 위치 index(ii): 기본 index / 레이블 index(li): 내가 설정한 index
    )                               # Series 클래스의 생성자 함수 호출

# 인덱스 호출 함수 loc함수: li 호출 / iloc함수: ii호출(iloc함수 많이 사용)

print(type(s1))
print(s1)