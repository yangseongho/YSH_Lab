def quick_sort(data):
    def quick_sort_recursive(A, left, right, comparisons, movements):
        if left < right:  # 정렬 범위가 2개 이상일 경우만 실행
            q, comparisons, movements = partition(A, left, right, comparisons, movements)
            comparisons, movements = quick_sort_recursive(A, left, q - 1, comparisons, movements)
            comparisons, movements = quick_sort_recursive(A, q + 1, right, comparisons, movements)
        return comparisons, movements

    def partition(A, left, right, comparisons, movements):
        pivot = A[left]  # 피벗은 리스트의 첫 번째 요소로 설정
        low = left + 1
        high = right

        while True:
            # 피벗보다 작은 값을 찾기 위해 low를 오른쪽으로 이동
            while low <= right and A[low] < pivot:
                low += 1
                comparisons += 1  # 비교 증가

            # 피벗보다 큰 값을 찾기 위해 high를 왼쪽으로 이동
            while high >= left and A[high] > pivot:
                high -= 1
                comparisons += 1  # 비교 증가

            if low < high:  # low와 high가 교차하지 않은 경우
                A[low], A[high] = A[high], A[low]
                movements += 2
            else:
                break

        # 피벗과 high 위치의 요소를 교환
        A[left], A[high] = A[high], A[left]
        movements += 2
        return high, comparisons, movements

    comparisons, movements = 0, 0
    comparisons, movements = quick_sort_recursive(data, 0, len(data) - 1, comparisons, movements)
    return comparisons, movements
