from CircularQueue import CircularQueue

queue = CircularQueue()

while True:
    command = input("[메뉴 선택] enqueue-e, dequeue-d, q-종료 => ")

    if command == 'e':
        item = int(input("enqueue할 요소를 입력하세요: "))
        queue.enqueue(item)
        print("현재 큐 상태:", queue)  # 큐 상태 출력

    elif command == 'd':
        queue.dequeue()
        print("현재 큐 상태:", queue)  # 큐 상태 출력

    elif command == 'q':
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 명령어입니다. 다시 입력하세요.")



