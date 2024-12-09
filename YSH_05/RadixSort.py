from queue import Queue
from collections import deque

def printStep(arr, val) :
    print("step%2d " % val, end='')
    print(arr)


def radix_sort(A):
    queues = []
    comparisons = 0
    movements = 0

    BUCKETS = 10  # 버킷은 항상 0~9로 고정
    max_value = max(A)
    DIGITS = len(str(max_value))  # 입력 데이터의 최대 자릿수 계산

    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS):
        # 자릿수에 따라 큐에 삽입
        for i in range(n):
            queues[(A[i] // factor) % BUCKETS].put(A[i])
            movements += 1  # 데이터 이동 (큐에 삽입)

        # 버킷에서 데이터를 꺼내어 리스트에 합친다
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                movements += 1  # 데이터 이동 (큐에서 꺼냄)
                i += 1

        factor *= 10  # 다음 자리수로 이동
        printStep(A, d + 1)

    return comparisons, movements
