import re

class ArrayList:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else : return None

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1) :
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else : pass

    def delete(self, pos):
        if not self.isEmpty() and 0<=pos<self.size :
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else : pass

    def replace(self, pos, new_content):
        if 0 <= pos < self.size:
            self.array[pos] = new_content
        else:
            print(f"유효하지 않은 행 번호입니다. (0 ~ {self.size - 1}) 범위에서 선택해주세요.")


    def make_dictionary(self):
        word_count = {}
        pattern = r'\b\w+\b'
        for i in range(self.size):
            line = self.getEntry(i)
            words = re.findall(pattern, line)
            for word in words:
                word = word.lower()  # 대소문자 구분
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        # 결과 출력
        print("단어 출현 빈도수:")
        for word, count in word_count.items():
            print(f"{word}: {count}")

        # dic.txt 파일에 저장
        with open("dic.txt", "w", encoding='utf-8') as outfile:
            for word, count in word_count.items():
                outfile.write(f"{word}: {count}\n")

    def __str__(self):
        return str(self.array[0:self.size])
