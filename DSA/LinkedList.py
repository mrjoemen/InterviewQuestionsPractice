from ast import Num
from operator import index
from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value) # initial value or head of the node
        self.index = 0
        self.length = 1

    def printList(self) -> None:
        currentNode = self.head
        self.index += 1
        while currentNode.next != None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
            self.index += 1
        print(currentNode.data)
        self.index = 0

    def appendNumber(self, value: Num) -> None:
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = Node(value)
        print(f"{value} added!")
        self.length += 1

    def appendAtIndex(self, value: int, index: int) -> None:
        currentNode = self.head
        if index > self.length:
            print(f"LinkedList Out of Bounds: The length of the current LinkedList is {self.length}")
            return

        if index == 0:
            placeHolder = self.head
            self.head = Node(value)
            self.head.next = placeHolder
            self.length += 1
            print(f"{value} added!")
            return
        
        if index == -1 or self.length == index:
            self.appendNumber(value)
            return

        while self.index < index:
            currentNode = currentNode.next
            self.index += 1

        if currentNode.next == None:
            currentNode.next == Node(value)
        else:
            upstream = currentNode.next
            currentNode.next = Node(value)
            currentNode.next.next = upstream
        self.index = 0
        self.length += 1
        print(f"{value} added!")
        return

    def deleteAtIndex(self, index: int) -> None:
        currentNode = self.head
        if index > self.length:
            print(f"LinkedList Out of Bounds: The length of the current LinkedList is {self.length}")
            return
        
        while self.index < index - 1:
            currentNode = currentNode.next
            self.index += 1

        placeHolder = currentNode.next.next
        itsValue = currentNode.next.data
        currentNode.next.next = None
        currentNode.next = placeHolder
        self.length -= 1
        print(f"{itsValue} deleted!")
        return

    def getLength(self) -> int:
        return self.length

def main():
    ll = LinkedList(9)
    ll.appendNumber(8)
    ll.appendNumber(10)
    ll.appendNumber(34)
    ll.appendAtIndex(32, 4)
    ll.appendAtIndex(100, 3)
    ll.appendAtIndex(7, 0)
    ll.printList()
    ll.deleteAtIndex(3)
    print(ll.getLength())
    ll.printList()


if __name__ == '__main__':
    main()