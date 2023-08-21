# data-algorithms

# Stack:
* Linear data structure, that follows the principle of __Last In First Out (LIFO)__.
* Basic Operations:
  * Push: Add an element to the top of stack
  * Pop: Remove an element from the top of stack
  * IsEmpty: Check if the stack is empty
  * IsFull: Check if the stack is full
  * Peek: Get the element from top of the stack without removing it.

## Stack Time Complexity
* The basic stack operation have a time complexity of $O(1)$, when implemented using array.
* Because the operations involve directly accessing or modifying the top element of the stack.
* There is no need to traverse the entire data structure.

## Application of Stack
* __To reverse a word__
* __In compilers__: used to calculate the value of expressions e.g.: 2+4/5*(5-2).
* __In browsers__: WEb pages visited in browser can be set on stack. The back and forward functionality in a browser is implement with stack.

# Queue : First In First Out (FIFO)
__Working with Queue__
  * Two pointers: `Front` and `Rare`
  * `Front`: tracks the first item
  * `Rare`: tracks the last item
  * `Front = -1` and `Rare = -1`, initially.
__List of Operations__
* Enqueue
  * Check if the queue is full
  * Set `Front = 0`, for the first item
  * Increase `Rare` by index 1
  * Enqueue the new item in the `Rare` index position
* Dequeue
  * Check if queue is empty
  * return value pointed by `Front`
  * Increase `Front` by 1
  * For the last element, set `Front` and `Rare` to -`.
* IsEmpty
* IsFull
* Peek

__Limitations of Queue__
* After queuing and queuing the size of queue is reduce
* The unused space can only be used after the queue is reset