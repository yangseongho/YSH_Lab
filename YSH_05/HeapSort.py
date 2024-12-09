def heapify(data, n, i, metrics):
    comparisons, movements = metrics
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        comparisons += 1
        if data[left] > data[largest]:
            largest = left

    if right < n:
        comparisons += 1
        if data[right] > data[largest]:
            largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        movements += 2
        # 재귀 호출의 반환값 처리
        data, sub_metrics = heapify(data, n, largest, (0, 0))
        sub_comparisons, sub_movements = sub_metrics
        comparisons += sub_comparisons
        movements += sub_movements

    return data, (comparisons, movements)


def heap_sort(data):
    comparisons, movements = 0, 0
    n = len(data)

    # 힙 빌드 과정
    for i in range(n // 2 - 1, -1, -1):
        data, (sub_comparisons, sub_movements) = heapify(data, n, i, (0, 0))
        comparisons += sub_comparisons
        movements += sub_movements

    # 정렬 과정
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # 루트와 마지막 원소 교환
        movements += 2
        data, (sub_comparisons, sub_movements) = heapify(data, i, 0, (0, 0))  # 힙 크기 감소 후 재정렬
        comparisons += sub_comparisons
        movements += sub_movements

    # 반환값을 기존 함수 호출부와 호환되도록 수정
    return comparisons, movements
