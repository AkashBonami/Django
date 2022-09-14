class linkedListNode :
    def __init__(self, value):
        self.value=value
        self.next=None

class linkedList :
    def __init__(self):
        self.head = None

    def ae(self , new) :
        if self.head is None :
            print("inside***********")
            self.head= linkedListNode(new)
        else: 
            print("ewor b**************")
            currentNode = self.head
            ne_val=linkedListNode( new)
            print(currentNode.value,'*************************')
            while True :
                if currentNode.next is None :
                    currentNode.next = ne_val 
                    break
            currentNode = currentNode.next 

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.value , "-->") 
            currentNode = currentNode.next
        print ("None")

ll=linkedList()
ll.ae(4)
ll.ae(6)
ll.ae(6)
ll.printLinkedList()