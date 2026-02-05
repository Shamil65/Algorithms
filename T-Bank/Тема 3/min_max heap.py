class MinHeap():


    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def insert(self, key, value):
        self.heap.append((key, value))
        self.sift_up(len(self.heap)-1)

    def peek_min(self):
        if not self.heap:
            raise IndexError("Пустая куча говна")
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            raise IndexError("Пустая куча говна")
        
        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self.sift_down(0)

        return min_element

    def heapify(self, elements):
        pass

    def meld(self, other_heap):
        pass

    def _parent(self, index):
        return (index - 1) // 2 if index != 0 else None

    def _left(self, index):
        left = index * 2 + 1
        return left if left < len(self.heap) else None

    def _right(self, index):
        right = index * 2 + 2
        return right if right < len(self.heap) else None

    def sift_up(self, index):
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = self._parent(index)

    def sift_down(self, index):
        pass
    

# готово?

