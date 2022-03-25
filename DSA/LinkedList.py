from ast import Num
from operator import index


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        self.node = Node(value) # initial value or head of the node
        self.index = 0

    def printList(self) -> None:
        print(self.node.data)
        self.index += 1
        while self.node.next != None:
            print(self.node.data)
            self.node = self.node.next
            self.index += 1
        self.index = 0

    def appendNumber(self, value: Num) -> None:
        if self.node.next == None: 
            self.node.next = Node(value)
            print(f"{value} added!")
            return
        while self.node.next != None:
            self.node = self.node.next
            self.index += 1
        self.node.next = Node(value)
        print(f"{value} added!")

def main():
    ll = LinkedList(9)
    ll.appendNumber(8)
    ll.printList()


if __name__ == '__main__':
    main()