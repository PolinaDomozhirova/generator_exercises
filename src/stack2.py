class SortedStack:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, value):
        # Находим место, куда вставить элемент, чтобы сохранить сортировку
        while self.stack and self.stack[-1] < value:
            self.temp_stack.append(self.stack.pop())
        self.stack.append(value)
        # Возвращаем элементы обратно из временного стека
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return not self.stack

# Пример использования
sorted_stack = SortedStack()
sorted_stack.push(6)
sorted_stack.push(9)
sorted_stack.push(2)
sorted_stack.push(5)

print(sorted_stack.pop())  # Вывод: 1
print(sorted_stack.pop())  # Вывод: 2
print(sorted_stack.pop())  # Вывод: 3
print(sorted_stack.pop())  # Вывод: 4
print(sorted_stack.pop())  # Вывод: Stack is empty