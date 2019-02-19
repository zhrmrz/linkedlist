class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def listLength(self):
        currentNode=self.head
        length=0
        while currentNode is not None:
            length+=1
            currentNode=currentNode.next
        return length
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode
    def printList(self):
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next
    def insertHead(self,newNode):
        temporarryNode=self.head
        self.head=newNode
        self.head.next=temporarryNode
        del temporarryNode
    def insertAt(self,newNode,position):
        if position<0 or position>self.listLength():
            print("Invalid")
            return
        if position==0:
            self.insertHead(newNode)
            return
        currentNode=self.head
        currenposition=0
        while True:
            if currenposition==position:
                previousNode.next=currentNode
                currentNode.next=newNode
                break
            previousNode=currentNode
            currentNode.next=currentNode
    def delEnd(self):
        lastNode=self.head
        while lastNode.next is not None:
            previousNode=lastNode
            lastNode=lastNode.next
        previousNode.next=None
    def delAt(self,position):
        if position<0 or position>=self.listLength():
            print("Invalid")
            return
        if self.isEmpty() is False:
            if position==0:
                self.delEnd()
                return
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition==position:
                previousNode.next=currentNode.next
                currentNode.next=None
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition+=1

if __name__ == '__main__':
    fNode=Node("John")
    linkedList=LinkedList()
    sNode=Node("Ben")
    linkedList.insert(fNode)
    linkedList.insert(sNode)
    linkedList.printList()
