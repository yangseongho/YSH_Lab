def shell_sort(data):
    n = len(data)
    gap = n // 2  # 초기 간격 설정

    # 비교와 이동 횟수 추적
    comparisons = 0
    movements = 0

    while gap > 0:

        # 간격을 기준으로 삽입 정렬 수행
        for start in range(gap):  # 각 부분 배열 시작점
            # 삽입 정렬 수행
            for i in range(start + gap, n, gap):
                key = data[i]
                j = i - gap

                # 삽입 정렬의 비교 및 이동 수행
                while j >= start and data[j] > key:
                    comparisons += 1  # 비교 증가
                    data[j + gap] = data[j]
                    movements += 1  # 이동 증가
                    j -= gap

                # 마지막 비교 수행
                if j >= start:
                    comparisons += 1  # 실패한 비교

                # 올바른 위치에 삽입
                data[j + gap] = key
                movements += 1  # 이동 증가

        # 간격을 절반으로 줄임
        gap //= 2

    return comparisons, movements
