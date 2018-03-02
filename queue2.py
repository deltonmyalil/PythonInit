'''a = [1,2,3,4]
a.append(5)
print(a)
a.insert(0,0)
print(a)
a.__delitem__(0)
print(a)
'''


queue = []
while(True):
    response = int(input("Select op : 1-EnQ; 2-DQ; 3-Disp; 4-exit>>>"))
    if response == 1:
        queue.append(input("Enter item to be enqueued>>>"))
    elif response == 2:
        if queue == []:
            print("Underflow")
        else:
            print("Dequeued item is ", queue[0])
            queue.__delitem__(0)
    elif response == 3:
        print(queue)
    elif response == 4:
        break