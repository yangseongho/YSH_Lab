from BinSrchTree import *

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.key, end=' ')   # node의 key만 중위순회로 출력
        inorder(n.right)

# 코드 9.11: 이진탐색트리를 이용한 맵 클래스
class BSTMap():
    def __init__ (self):
        self.root = None

    def isEmpty (self):
       return self.root == None

    def findMax(self):
       return search_max_bst(self.root)

    def findMin(self):
       return search_min_bst(self.root)

    def search(self, key):
       return search_bst(self.root, key)
       #return search_bst_iter(self.root, key)

    def searchValue(self, key):
       return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty() :
           self.root = n
        else :
           insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst (self.root, key)

    def display(self, msg = 'BTSMap :'):
        print(msg, end='')
        inorder(self.root)
        print()


#=========================================================
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
# 코드 9.12: 이진탐색트리를 이용한 맵 테스트 프로그램
if __name__ == "__main__":
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value= ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

    map = BSTMap()
    map.display("[삽입 전] : ")
    for i in range(len(data)) :
        map.insert(data[i],value[i])
        map.display("[삽입 %2d] : "%data[i])

    print('[최대 키] : ', map.findMax().key)
    print('[최소 키] : ', map.findMin().key)
    print('[탐색 26] : ', '성공' if map.search(26) != None else '실패')
    print('[탐색 25] : ', '성공' if map.search(25) != None else '실패')
    print('[탐색 일팔]:', '성공' if map.searchValue("일팔") != None else '실패')
    print('[탐색 일칠]:', '성공' if map.searchValue("일칠") != None else '실패')
    
    map.delete(3)
    map.display("[삭제  3] : ")
    map.delete(68)
    map.display("[삭제 68] : ")
    map.delete(18) 
    map.display("[삭제 18] : ")
    map.delete(35) 
    map.display("[삭제 35] : ")
