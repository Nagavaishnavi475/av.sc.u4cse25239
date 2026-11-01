class BinaryHeap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type.lower()

    def _compare(self, parent_val, child_val):
        if self.heap_type == "max":
            return parent_val < child_val  # Max Heap: Parent should be >= Child
        else:
            return parent_val > child_val  # Min Heap: Parent should be <= Child

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
        print(f"Successfully inserted {key}.")

    def delete_root(self):
        if not self.heap:
            print("Heap underflow! The heap is currently empty.")
            return None

        root_val = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._heapify_down(0)

        print(f"Successfully deleted root node ({root_val}).")
        return root_val

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.heap[parent], self.heap[index]):
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        extreme_index = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Check if left child breaks the heap property
        if left < size and self._compare(self.heap[extreme_index], self.heap[left]):
            extreme_index = left

        # Check if right child breaks the heap property
        if right < size and self._compare(self.heap[extreme_index], self.heap[right]):
            extreme_index = right

        # Swap and continue heapifying if a child broke the rule
        if extreme_index != index:
            self.heap[index], self.heap[extreme_index] = self.heap[extreme_index], self.heap[index]
            self._heapify_down(extreme_index)

    def display(self):
        """Displays the array representation of the heap."""
        if not self.heap:
            print("The heap is empty.")
        else:
            print(f"{self.heap_type.capitalize()} Heap Array: {self.heap}")


def main():
    print("--- Binary Heap Implementation ---")
    while True:
        heap_choice = input("Choose Heap Type:\n1. Min Heap\n2. Max Heap\nChoice (1 or 2): ").strip()
        if heap_choice == '1':
            h = BinaryHeap(heap_type="min")
            break
        elif heap_choice == '2':
            h = BinaryHeap(heap_type="max")
            break
        else:
            print("Invalid selection. Please enter 1 or 2.\n")

    while True:
        print(f"\n======== {h.heap_type.upper()} HEAP OPERATIONS ========")
        print("1. Insertion of an element")
        print("2. Deletion of the root element")
        print("3. Display the array representation")
        print("4. Exit program")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            try:
                val = int(input("Enter an integer value to insert: "))
                h.insert(val)
            except ValueError:
                print("Error: Please enter a valid integer.")
        
        elif choice == '2':
            h.delete_root()
        
        elif choice == '3':
            h.display()
        
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        
        else:
            print("Invalid input! Please choose an option between 1 and 4.")

if __name__ == "__main__":
    main()
