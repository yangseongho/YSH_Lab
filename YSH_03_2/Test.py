import heapq


# 코드 8.1: Huffman Tree를 위한 노드 클래스
class Node:
    def __init__(self, char, freq):
        self.char = char  # 문자
        self.freq = freq  # 빈도수
        self.left = None  # 왼쪽 자식
        self.right = None  # 오른쪽 자식

    # 비교 연산자 정의 (빈도수를 기준으로 힙에 적합하게 비교)
    def __lt__(self, other):
        return self.freq < other.freq


# 코드 8.2: Huffman Coding 알고리즘
def build_huffman_tree(chars, freqs):
    # 1. 빈도수를 기준으로 노드들을 min heap에 삽입
    heap = []
    for i in range(len(chars)):
        heapq.heappush(heap, Node(chars[i], freqs[i]))

    # 2. 최소 힙을 사용하여 트리를 구축
    while len(heap) > 1:
        left = heapq.heappop(heap)  # 가장 작은 두 노드를 꺼냄
        right = heapq.heappop(heap)

        # 두 노드를 합쳐 새로운 노드를 생성
        merged = Node(None, left.freq + right.freq)  # 문자 없음, 빈도수만 합침
        merged.left = left
        merged.right = right

        # 새로 만든 노드를 다시 힙에 삽입
        heapq.heappush(heap, merged)

    # 3. 트리가 하나의 루트 노드로 남게 되면 그 노드를 반환
    return heap[0]


# 코드 8.3: Huffman 코드 생성
def generate_huffman_codes(root, prefix='', codes={}):
    if root is not None:
        if root.char is not None:  # 리프 노드일 경우
            codes[root.char] = prefix
        generate_huffman_codes(root.left, prefix + '0', codes)  # 왼쪽 자식으로 0
        generate_huffman_codes(root.right, prefix + '1', codes)  # 오른쪽 자식으로 1
    return codes


# 코드 8.4: 문자 인코딩
def encode_message(message, huffman_codes):
    encoded_message = ''.join(huffman_codes[char] for char in message)
    return encoded_message


# 코드 8.5: 압축률 계산
def calculate_compression_rate(original, encoded):
    original_bits = len(original) * 8  # 원본 데이터 비트 수 (1문자 = 8비트)
    encoded_bits = len(encoded)  # 인코딩된 비트 수
    return (original_bits - encoded_bits) / original_bits * 100


# 코드 8.6: 메인 함수
if __name__ == "__main__":
    # 문자와 빈도수
    chars = ['k', 'o', 'r', 'e', 'a', 't', 'c', 'h']
    freqs = [10, 5, 2, 15, 18, 4, 7, 11]

    # 1. Huffman 트리 생성
    root = build_huffman_tree(chars, freqs)

    # 2. Huffman 코드 생성
    huffman_codes = generate_huffman_codes(root)

    print("Huffman Codes:", huffman_codes)

    # 3. 입력 문장 받기
    message = input("Please a word: ").strip()

    # 4. 유효한 문자 확인 (허용된 문자만 인코딩)
    if any(c not in huffman_codes for c in message):
        print("illegal character")
    else:
        # 5. 메시지 인코딩
        encoded_message = encode_message(message, huffman_codes)
        print("결과 비트 열:", encoded_message)

        # 6. 압축률 계산
        compression_rate = calculate_compression_rate(message, encoded_message)
        print(f"압축률: {compression_rate:.2f}%")
