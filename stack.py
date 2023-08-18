# stack implementation in python

class Stack:
    def __init__(self):
        self._stack = []

    def display_stack(self):
        return self._stack

    def push(self, value):
        self._stack.append(value)
        print("Pushed Item:", value)

    def isEmpty(self):
        return len(self._stack) == 0

    def pop(self):
        if self.isEmpty():
            return "stack empty, pop operation cannot be performed"

        return self._stack.pop()

    def peek(self):
        if self.isEmpty():
            return "stack empty, peek operation cannot be performed"
        stack_size = len(self._stack)
        return self._stack[stack_size-1]


st = Stack()
for i in range(6):
    st.push(i)

boolean = st.isEmpty()
print("stack is empty: ", boolean)
print("\n")

print("stack before pop: ", st.display_stack())
pop_returns = st.pop()
print("pop returns: ", pop_returns)
print("stack after pop: ", st.display_stack())
print("\n")

print("stack before peek: ", st.display_stack())
peek_returns = st.peek()
print("peek returns: ", peek_returns)
print("stack after peek: ", st.display_stack())
