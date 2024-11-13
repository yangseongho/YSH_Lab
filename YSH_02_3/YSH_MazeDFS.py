from YSH_ArrayStack import ArrayStack

# 10x10 미로 맵 정의 (0: 통로, 1: 벽, x: 출구)
map = [ ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '1', '1', '0', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '1', '0', '0', '1'],
        ['1', '0', '1', '1', '1', '0', '1', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1', '0', '0', '0', '0', '1'],
        ['1', '1', '1', '0', '1', '0', '1', '1', '0', 'x'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

MAZE_SIZE = 10

def isVaildPos(x, y) :
    if 0 <= x < MAZE_SIZE and 0 <= y< MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def DFS():
    print('DFS: ')
    stack = ArrayStack(100)
    stack.push((0, 1))
    move_count = 0

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end='->')
        (x, y) = here

        if (map[y][x] == 'x'):
            print(" 미로 탐색 성공!")
            print(f"이동거리 = {move_count}")
            return True

        else:
            map[y][x] = '.'
            move_count += 1

            if isVaildPos(x, y - 1): stack.push((x, y - 1))  # 상
            if isVaildPos(x, y + 1): stack.push((x, y + 1))  # 하
            if isVaildPos(x - 1, y): stack.push((x - 1, y))  # 좌
            if isVaildPos(x + 1, y): stack.push((x + 1, y))  # 우

        print('현재 스택 :', stack)



    return False

