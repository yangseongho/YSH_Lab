sorted = [0]*100
# 코드 12.6: 병합 정렬
def merge_sort(A, left, right):
    comparisons = 0
    movements = 0
    if left < right:
        mid = (left + right) // 2  # 리스트의 균등 분할
        comparisons_left, movements_left = merge_sort(A, left, mid)  # 부분 리스트 정렬
        comparisons_right, movements_right = merge_sort(A, mid + 1, right)  # 부분 리스트 정렬
        comparisons_merge, movements_merge = merge(A, left, mid, right)  # 병합

        # 전체 비교 연산과 데이터 이동 수를 합산
        comparisons += comparisons_left + comparisons_right + comparisons_merge
        movements += movements_left + movements_right + movements_merge

    return comparisons, movements


# 코드 12.7: 병합 정렬을 위한 merge() 함수
def merge(A, left, mid, right):
    comparisons = 0  # 비교 횟수
    movements = 0  # 데이터 이동 횟수
    i, j, k = left, mid + 1, left  # i: 왼쪽 배열, j: 오른쪽 배열, k: 병합 배열 인덱스

    # 병합 시작
    while i <= mid and j <= right:
        comparisons += 1  # 비교 횟수 증가
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i += 1
        else:
            sorted[k] = A[j]
            j += 1
        k += 1
        movements += 1  # 데이터를 임시 배열로 복사

    # 남아 있는 왼쪽 배열 복사
    while i <= mid:
        sorted[k] = A[i]
        i += 1
        k += 1
        comparisons += 1
        movements += 1

    # 남아 있는 오른쪽 배열 복사
    while j <= right:
        sorted[k] = A[j]
        j += 1
        k += 1
        comparisons += 1
        movements += 1

    # 임시 배열을 원래 배열로 복사
    for idx in range(left, right + 1):
        A[idx] = sorted[idx]
        movements += 1  # 원래 배열로 복사 시 이동 횟수 증가

    return comparisons, movements

# 테스트 프로그램
if __name__ == "__main__":
    data = [5, 3, 8, 4, 1, 6, 2, 7, 9]
    print("Original  : ", data)
    comparisons, movements = merge_sort(data, 0, len(data)-1)
    print("Merge     : ", data)
    print("Number of Comparisons:", comparisons)
    print("Number of Data Movements:", movements)
