from HeapSort import heap_sort
from QuickSort import quick_sort
from RadixSort import radix_sort
from ShellSort import shell_sort
from mergeSort import merge_sort

# Selection Sort
def selection_sort(A):
    n = len(A)
    comparisons, movements = 0, 0
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            comparisons += 1
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        movements += 2
    return comparisons, movements

# Insertion Sort
def insertion_sort(A):
    n = len(A)
    comparisons, movements = 0, 0
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            comparisons += 1
            A[j + 1] = A[j]
            movements += 1
            j -= 1
        comparisons += 1  # 마지막 비교 (while 종료 조건)
        A[j + 1] = key
        movements += 1
    return comparisons, movements

# Bubble Sort
def bubble_sort(A):
    n = len(A)
    comparisons, movements = 0, 0
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            comparisons += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                movements += 2
                bChanged = True
        if not bChanged:
            break
    return comparisons, movements


def execute_sorting_algorithm(algorithm, arr):
    # 주어진 알고리즘에 따라 정렬 수행
    if algorithm == "SEL":
        return selection_sort(arr)
    elif algorithm == "INS":
        return insertion_sort(arr)
    elif algorithm == "BUB":
        return bubble_sort(arr)
    elif algorithm == "SHE":
        return shell_sort(arr)
    elif algorithm == "HEA":
        return heap_sort(arr)
    elif algorithm == "MER":
        return merge_sort(arr, 0, len(arr)-1)
    elif algorithm == "QUI":
        return quick_sort(arr)
    elif algorithm == "RAD":
        return radix_sort(arr)
    else:
        raise ValueError("지원하지 않는 정렬 알고리즘입니다.")


if __name__ == "__main__":
    print("* Please input a data list :")
    try:
        data = list(map(int, input().split(",")))
    except ValueError:
        print("올바른 형식의 숫자 리스트를 입력하세요. 예: 1,2,3,4")
        exit()

    print(
        "* Target Sorting Algorithm List: Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE), Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)"
    )
    algorithm = input("* Select sorting algorithm: ").strip().upper()

    original_data = data[:]
    try:
        comparisons, movements = execute_sorting_algorithm(algorithm, data)
        print(f">> Original: {original_data}")
        print(f">> Sorted  : {data}")
        print(f">> Number of Comparisons: {comparisons}")
        print(f">> Number of Data Movements: {movements}")
    except ValueError as e:
        print(e)
