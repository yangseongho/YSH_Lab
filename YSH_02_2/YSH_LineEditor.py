from YSH_ArrayList import ArrayList

list = ArrayList()

while True :
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, m-빈도 수 확인 q-종료 =>")

    if command == 'i':
        pos = int(input("입력 행 번호 :"))
        str = input("입력 행 내용 :")
        list.insert(pos, str)

    elif command == 'd':
        pos = int(input("삭제 행 번호 :"))
        list.delete(pos)

    elif command == 'r':
        pos = int(input("변경 행 번호 :"))
        new_content = input("변경 행 내용 :")
        list.replace(pos, new_content)

    elif command == 'p':
        print('Line Editor')
        for line in range (list.size) :
            print('[%2d]' %line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q' : exit()

    elif command == 'l' :
        filename = 'test.txt'
        infile = open(filename, "r", encoding='utf-8')
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's' :
        fliename = 'test.txt'
        outflie = open(fliename, "w", encoding='utf-8')
        len = list.size
        for i in range(len) :
            outflie.write(list.getEntry(i)+'\n')
        outflie.close()

    elif command == 'm' :
        list.make_dictionary()



