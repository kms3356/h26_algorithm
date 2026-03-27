def st_push(stack):
    if len(stack) == 5:
        print("> Stack이 차 있어서 더 이상 추가할 수 없습니다.")
        print("> 현재 스택 상태 ", stack)
    else:
        x = input("데이터 입력 : ")
        stack.append(x)
        print("> 현재 스택 상태 ", stack)

def st_pop(stack):
    if stack:
        print("> 가져온 데이터 : ", stack.pop())
        print("> 현재 스택 상태 ", stack)
    else:
        print("> Stack이 비어 있습니다.")
        print("> 현재 스택 상태 ", stack)

def st_peek(stack):
    if stack:
        print("> 최상단 데이터 : ", stack[-1])
        print("> 현재 스택 상태 ", stack)
    else:
        print("> Stack이 비어 있습니다.")
        print("> 현재 스택 상태 ", stack)

def solve():

    stack = []
    print("---[ 정수형 스택 연산 실습 (용량 5)]---")
    while True:
        print("=============================")
        print("1.Push, 2.Pop, 3.Peek 0.Exit")
        print("=============================")
        n = input(">메뉴선택 : ")
        match n:
            case '1':
                st_push(stack)
            case '2':
                st_pop(stack)
            case '3':
                st_peek(stack)
            case '0':
                print("---[ 정수형 스택 연산 실습 종료 ]---")
                break            

solve()