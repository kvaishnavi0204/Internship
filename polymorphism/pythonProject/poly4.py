L1={12,23,45,64,76,43}
key=64
for i in L1:
    if (i == key):
        print( 'key found at index',Index{i})

from typing import Any, Generator

arr=input("enter the list of numbers separated by spaces:").split()
arr=[int(x) for x in arr]

target = int(input("enter the target value to search:"))
found = False


for i in range (len(arr)):
    if arr[i] == target:
        print(f"Target{target}found at index {i}.")
        found = True
        break

if not found:
    print(f"Target{target}not found in the array.")

arr =[int(x) for x in input("enter the sorted list of numbers separated by space").split()]
target = int(input("enter the target value to search:"))
start,end = 0,len(arr) -1
found = False
while start <= end:
    mid = (start + end)//2
    if arr[mid] == target:
        print(f"Target{target}found at index {mid}.")
        found = True
        break
    elif arr[mid]<target:
        start = mid +1
    else:
        end = mid - 1

if not found:
    print(f"Target {target} not found in the array.")

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j] ,arr[j+1] = arr[j+1],arr[j]

my_list=[56,34,78,54,98,32,44]
print("originalmlist:",my_list)
bubble_sort(my_list)
print("sorted list;",my_list)


class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
    def size(self):
        return len(self.items)
stack =Stack()
print("is the stack empty?",stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print("stack:",stack.items)
print("top of the stack:",stack.peek())
print("pop:",stack.pop())
print("stack after the pop",stack.items)
print("is the stack empty?",stack.is_empty())
print("size of the stack:",stack.size())

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None
    def push(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node
    def pop(self):
        if self.is_empty():
            return None
        popped = self.head.data
        self.head =self.head.next
        return popped
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("popped:",stack.pop())
print("peek:",stack.peek())
stack.display()

class QueueList:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")

    def size(self):
         return len(self.items)
queue = QueueList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("front of the queue:",queue.peek())
print("dequeue:",queue.dequeue())
print("size of the queue:",queue.size())
