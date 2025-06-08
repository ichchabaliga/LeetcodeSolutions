# Last updated: 08/06/2025, 13:56:31
# 2 items have same f? LRU
# counter=minfreq
# Hash{key,(value,freq)}
# hasset{freq:[LinkedList[keys]]}
# Append MRU to the linkedList which has the key==freq of the current key 
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size = 0



    def add(self, node):
        self.head.next.prev=node
        node.next=self.head.next
        self.head.next=node
        node.prev=self.head
        self.size +=1

        
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self.size -=1

        
    def getLastNode(self):
        if self.size>0:
            node=self.tail.prev
            return node
        return None
    


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.freq_map=defaultdict(DoublyLinkedList)
        self.min_freq=0

    

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node=self.cache[key]
        self.update(node)
        return node.value

    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node=self.cache[key]
            node.value = value
            self.update(node)
            return

        if len(self.cache) >= self.capacity:
            # performeviction
            min_list=self.freq_map[self.min_freq]
            remove_node=min_list.getLastNode()
            min_list.remove(remove_node)
            del self.cache[remove_node.key]

        new_node=Node(key,value)
        self.cache[key]=new_node
        self.freq_map[1].add(new_node)
        self.min_freq=1

    
    def update(self, node):
        # Remove from current frequency list
        self.freq_map[node.freq].remove(node)
        if self.freq_map[node.freq].size==0:
            del self.freq_map[node.freq]
            if node.freq==self.min_freq:
                self.min_freq+=1

        node.freq+=1
        self.freq_map[node.freq].add(node)
      

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)