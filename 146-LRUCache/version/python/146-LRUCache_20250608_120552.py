# Last updated: 08/06/2025, 12:05:52
# Not null
# cofigurable capicity 
# get(key): O(1) Hashmaps
# put(Key,value):O(N), O(1) DOubleLinkedList 

# Coreentities:Key and value
# Classes: Node
# LRU

class ListNode:
    def __init__(self,key,value):
        self.prev=None
        self.next=None
        self.key=key
        self.value=value

class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.store={}
        self.LRUQueue_head=ListNode(-1,-1)
        self.LRUQueue_tail=ListNode(-1,-1)
        self.LRUQueue_head.next=self.LRUQueue_tail
        self.LRUQueue_tail.prev=self.LRUQueue_head
        
    def get(self,key):
        if not key in self.store:
            return -1
        node=self.store[key]
        self.remove(node)
        self.add(node)
        return node.value


    def put(self,key,value):
        if key in self.store:
            node=self.store[key]
            self.remove(node)
            
        
        node=ListNode(key,value)
        self.store[key]=node
        self.add(node)
        if len(self.store)>self.capacity:
            node_to_remove=self.LRUQueue_head.next
            self.remove(node_to_remove)
            del self.store[node_to_remove.key]
        

        
#Remove from the list 
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        
#add to the back of the list 
    def add(self,node):
        self.LRUQueue_tail.prev.next=node
        node.next=self.LRUQueue_tail
        node.prev=self.LRUQueue_tail.prev
        self.LRUQueue_tail.prev=node

        

# class ListNode:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.prev=None
#         self.next=None

# class LRUCache:
#     def __init__(self, size):
#         self.capacity=size
#         self.store = defaultdict()
#         self.head= ListNode(-1,-1)
#         self.tail=ListNode(-1,-1)
#         self.head.next=self.tail
#         self.tail.prev=self.head
    
#     def get(self,key):
#         if not key in self.store:
#             return -1

#         node=self.store[key]
#         self.remove(node)
#         self.add(node)
#         return node.value
    
#     def put(self,key,value):
#         if key in self.store:
#             oldNode=self.store[key]
#             self.remove(oldNode)
#         node=ListNode(key,value)
#         self.store[key]=node
#         self.add(node)
#         if len(self.store)>self.capacity:
#             node=self.head.next
#             self.remove(node)
#             del self.store[node.key]
#         return 

    
        
        
   
#     def remove(self,node):
#         node.prev.next, node.next.prev =node.next, node.prev
#     def add(self,node):
#         node.prev=self.tail.prev
#         node.next=self.tail
#         self.tail.prev.next=node
#         self.tail.prev=node

    

