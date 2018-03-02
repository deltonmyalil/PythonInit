top = 0
stack = [0 for x in range(10)]
while(True):
    response = input("Push(1) or pop(2) or print stack(3) or exit(0)?>>>")
    if response == '1':
        if top == 10:
            print("Overflow")
        else:
            stack[top] = input("Enter the element to push>>>")
            top += 1
    elif response == '2':
        if top == 0:
            print("Underflow")
        else:
            print("element popped is",stack[top-1])
            top -= 1
    elif response == '3':
        print(stack)
    elif response == '0':
        print("exiting...")
        break