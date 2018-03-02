front = -1
rear = -1
queue = [0 for x in range(10)]

while(True):
    response = input("Enter Operation\n1. Enqueue\n2. Dequeue\n3. Display\n4. exit>>>")
    if response == '1': # enqueue
        if rear == 10-1:
            print("Overflow\n")
        else:
            if front == -1:
                front = 0
            rear += 1
            queue[rear] = input("Enter item to be enqueued>>>")
    elif response == '2':  # dequeue
        if front == -1 or front > rear:
            print("underflow")
        else:
            print("Dequeued item is - ", queue[front])
            queue[front] = 0
            front += 1
    elif response == '3':
        print(queue)
    elif response == '4':
        break