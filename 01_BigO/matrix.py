import time, random

def sum_matrix(A, n):
    B = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i] + A[j]


# n = 1 이상 5000 이하 정수 값 입력
n = int(input())
# 리스트 A에 랜덤 정수 값 n개 채움
A = [random.randint(1, n) for _ in range(n)]
# sum 함수 호출 + 시간 측정
before = time.process_time()
sum_matrix(A, n)
after = time.process_time()
time = after - before
# 함수의 수행시간을 출력
print(f"실행시간: {time:.6f} 초")
