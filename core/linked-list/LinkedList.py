from typing import List


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if index == 0:
            if not self.head:
                return False
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True

        curr = self.head
        i = 0
        while curr and curr.next:
            if i == index - 1:
                curr.next = curr.next.next
                if not curr.next:
                    self.tail = curr
                return True
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
