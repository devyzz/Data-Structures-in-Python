import time
import random

def prefixSum1(X, n):
    """ O(n^2) 알고리즘 - 이중 반복문을 사용한 prefix sum """
    S = [0] * n  # 리스트를 0으로 초기화
    for i in range(n):
        S[i] = 0  # 필요 없음 (S[i]는 이미 0으로 초기화됨)
        for j in range(i + 1):  # i까지 포함해야 함
            S[i] += X[j]
    return S

def prefixSum2(X, n):
    """ O(n) 알고리즘 - 누적 합을 이용한 prefix sum """
    S = [0] * n
    S[0] = X[0]  # 첫 번째 요소 초기화
    for i in range(1, n):
        S[i] = S[i - 1] + X[i]  # 바로 이전 값에 현재 값을 더함
    return S

random.seed()  # random 함수 초기화

# n 입력받음
n = int(input("n을 입력하세요: "))

# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X = [random.randint(1, n) for _ in range(n)]  # 1~n 범위 난수 생성

# prefixSum1 호출 및 실행 시간 측정
before = time.process_time()
S1 = prefixSum1(X, n)
after = time.process_time()
time1 = after - before

# prefixSum2 호출 및 실행 시간 측정
before = time.process_time()
S2 = prefixSum2(X, n)
after = time.process_time()
time2 = after - before

# 두 함수의 수행시간 출력
print(f"실행시간1 (O(n^2)): {time1:.6f} 초")
print(f"실행시간2 (O(n)): {time2:.6f} 초")
