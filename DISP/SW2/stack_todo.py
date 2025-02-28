"""
Context:
In a medical software system, a stack could track a series of "undo" operations for
changes to patient records—Last In, First Out (LIFO).

Exercise:
Implement a Stack class with:
- push(item)
- pop()
- is_empty()

Demonstrate how you might record edits and then pop the most recent edit for an undo.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    edit_stack = Stack()
    edit_stack.push("Edit1: Added new lab result")
    edit_stack.push("Edit2: Changed dosage info")

    last_edit = edit_stack.pop()
    print("Undo operation:", last_edit)
