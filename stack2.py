stack = []
while(True):
    response = int(input("Enter Op: 1-Push; 2-Pop; 3-Disp; 4-Exit>>>"))
    if response == 1:
        stack.insert(0,input("Enter item to push>>>"))
    elif response == 2:
        if stack == []:
            print("Underflow")
        else:
            print("Dequeued item ", stack[0])
            stack.__delitem__(0)
    elif response == 3:
        print(stack[::-1])
    elif response == 4:
        break