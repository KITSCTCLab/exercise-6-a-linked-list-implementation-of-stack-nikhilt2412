class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    nn = Node(data)
    nn.next = self.head
    self.head = nn

  def pop(self) -> None:
    temp = self.head
    self.head = temp.next

  def status(self):
    """
    It prints all the elements of stack.
    """
    temp = self.head
    while temp.next!= None:
      print(temp.data)
      temp = temp.next

# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
