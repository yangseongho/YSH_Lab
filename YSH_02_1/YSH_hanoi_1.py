import time

def hanoi_tower(n, fr, tmp, to, counter) :
    if n == 1:
        print("원판 1 : %s --> %s" % (fr, to))

        counter[0] += 1 # 호출 횟수 증가

    else :
        hanoi_tower(n - 1, fr, to, tmp, counter)
        print("원판 %d : %s --> %s" % (n, fr, to))
        counter[0] += 1 # 호출 횟수 증가
        hanoi_tower(n - 1, tmp, fr, to, counter)

def runtime_hanoi_tower(n) :
    counter = [0]  # 호출 횟수를 저장할 리스트
    start = time.time()  # 시작 시간

    hanoi_tower(n, 'A','B', 'C', counter)

    end = time.time()  # 종료 시간

    print(f"hanoi_tower 함수 호출 횟수: {counter[0]}")
    print("실행 시간 : ", end-start)