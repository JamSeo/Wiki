class Queue:
    # creatQueue, 만들 큐의 크기를 받자.
    def __init__(self, n):
        self.size = n
        self.items = [None] * n
        self.rear = -1
        self.front = -1

    # 큐에 아이템 추가
    def enQueue(self, item):
        if self.isFull():
            print('Queue is Full')
        else:
            self.rear += 1
            self.items[self.rear] = item

    # 큐에 아이템 제거
    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            self.front += 1
            return self.items[self.front]

    # 큐가 비어있는지
    def isEmpty(self):
        return self.front == self.rear

    # 큐가 가득찼는지
    def isFull(self):
        return self.rear == self.size - 1
    
    # 앞에 나올 예정인 것 확인
    def peek(self):
        return self.items[self.front]
    
    # dunder method 로써
    # len 함수의 인자로 활용되었을 때의 반환 정의
    def __len__(self):
        return self.rear - self.front


q = Queue(3)
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())