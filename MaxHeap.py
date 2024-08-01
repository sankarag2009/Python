# this module is to impliment python Binary Heap Data Structure
class MaxHeap:
    # heap list declaration
    heap=[]
    # intialize max heap to 0
    maxheapsize=0
    #intial binary tree size is 0
    heapsize=0
#    Constructor sets the intial params for the heap
    def __init__(self, maxheapsize) -> None:
        self.maxheapsize=maxheapsize
        self.heap=[None]*maxheapsize
        self.heapsize=0
#  Heapifies the tree taking the max as root
    def MaxHeapify(self, i):
        lc = self.lChild(i) 
        rc = self.rChild(i) 
        largest = i 
        if lc < self.heapsize and self.heap[lc] > self.heap[i]: 
            largest = lc 
        if rc < self.heapsize and self.heap[rc] > self.heap[largest]: 
            largest = rc 
        if largest != i: 
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i] 
            self.MaxHeapify(largest)

 # Returns the index of the parent 
    # of the element at ith index. 
    def parent(self, i): 
        return (i - 1) // 2
  
    # Returns the index of the left child. 
    def lChild(self, i): 
        return (2 * i + 1) 
  
    # Returns the index of the 
    # right child. 
    def rChild(self, i): 
        return (2 * i + 2) 
  
    # Removes the root which in this 
    # case contains the maximum element. 
    def removeMax(self): 
        # Checking whether the heap heapay 
        # is empty or not. 
        if self.heapsize <= 0: 
            return None
        if self.heapsize == 1: 
            self.heapsize -= 1
            return self.heap[0] 
  
        # Storing the maximum element 
        # to remove it. 
        root = self.heap[0] 
        self.heap[0] = self.heap[self.heapsize - 1] 
        self.heapsize -= 1
  
        # To restore the property 
        # of the Max heap. 
        self.MaxHeapify(0) 
  
        return root 
  
    # Increases value of key at 
    # index 'i' to new_val. 
    def increaseKey(self, i, newVal): 
        self.heap[i] = newVal 
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]: 
            temp = self.heap[i] 
            self.heap[i] = self.heap[self.parent(i)] 
            self.heap[self.parent(i)] = temp 
            i = self.parent(i) 
  
    # Returns the maximum key 
    # (key at root) from max heap. 
    def getMax(self): 
        return self.heap[0] 
  
    def curSize(self): 
        return self.heapsize 
  
    # Deletes a key at given index i. 
    def deleteKey(self, i): 
        # It increases the value of the key 
        # to infinity and then removes 
        # the maximum value. 
        self.increaseKey(i, float("inf")) 
        self.removeMax() 
  
    # Inserts a new key 'x' in the Max Heap. 
    def insertKey(self, x): 
        # To check whether the key 
        # can be inserted or not. 
        if self.heapsize == self.maxheapsize: 
            print("\nOverflow: Could not insertKey\n") 
            return
        # The new key is initially 
        # inserted at the end. 
        self.heapsize += 1
        i = self.heapsize - 1
        self.heap[i] = x 
  
        # The max heap property is checked 
        # and if violation occurs, 
        # it is restored. 
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]: 
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i] 
            i = self.parent(i) 
  
  
# Driver program to test above functions. 
if __name__ == '__main__': 
    # Assuming the maximum size of the heap to be 15. 
    h = MaxHeap(15) 
  
    # Asking the user to input the keys: 
    k, i, n = 6, 0, 6
    print("Entered 6 keys:- 3, 10, 12, 8, 2, 14 \n") 
    h.insertKey(3) 
    h.insertKey(10) 
    h.insertKey(12) 
    h.insertKey(8) 
    h.insertKey(2) 
    h.insertKey(14) 
  
    # Printing the current size 
    # of the heap. 
    print("The current size of the heap is "
          + str(h.curSize()) + "\n") 
  
    # Printing the root element which is 
    # actually the maximum element. 
    print("The current maximum element is " + str(h.getMax()) 
          + "\n") 
  
    # Deleting key at index 2. 
    h.deleteKey(2) 
  
    # Printing the size of the heap 
    # after deletion. 
    print("The current size of the heap is "
          + str(h.curSize()) + "\n") 
  
    # Inserting 2 new keys into the heap. 
    h.insertKey(15) 
    h.insertKey(5) 
    print("The current size of the heap is "
          + str(h.curSize()) + "\n") 
    print("The current maximum element is " + str(h.getMax()) 
          + "\n")                            