"""
n_c_list = []
outstr = ''
outarr = []
digits = ['0', '1', '2', '3', '4', '5']
inarr = ['30012', '250232', '53201', '3004355', '124111']
# inarr = ['01221', '21313', '12321']
for i in range(len(inarr) - 1):
    un_string = inarr[i]
    for j in range(len(inarr)):
        if j > i + 1:
            n_c_list.append(un_string + inarr[j])
for item in n_c_list:
    flag = False
    for digit in digits:
        if digit not in item:
            flag = True
    if not flag:
        outarr.append(item)

if len(outarr) == 0:
    outstr = -1
    print(outstr)
else:
    maxlen = -1
    for item in outarr:
        if len(item) > maxlen:
            maxlen = len(item)
            outstr = item
    print(outstr)
"""

"""
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def reorder_elements(input_list):
    head = input_list.get_head()
    next_node = head.get_next()
    while head is not None and next_node.get_next() is not None:
        val = next_node.get_data()*2
        head.set_data(val)
        head = head.get_next()
        next_node = head.get_next()
        if next_node is not None:
            next_node.set_data(next_node.get_data()*2)


linklist = LinkedList()
linklist.add(3)
linklist.add(8)
linklist.add(15)
linklist.add(21)
linklist.display()
print(linklist)
reorder_elements(linklist)
print(linklist)
"""

"""
class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index])

    def __str__(self):
        msg = []
        index = self.__front
        while index <= self.__rear:
            msg.append(str(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg


def rearrange_fruits(fruits):
    out_queue = Queue(fruits.get_max_size())
    queue1 = Queue(fruits.get_max_size())
    queue2 = Queue(fruits.get_max_size())
    vowels = ['a', 'e', 'i', 'o', 'u']
    while not fruits.is_empty():
        count = 0
        data = fruits.dequeue()
        for char in data:
            if char in vowels:
                count += 1
        if count % 2 == 0:
            queue1.enqueue(data)
        else:
            queue2.enqueue(data)
    while not queue2.is_empty():
        out_queue.enqueue(queue2.dequeue())

    while not queue1.is_empty():
        out_queue.enqueue(queue1.dequeue())
    return out_queue


fruits = Queue(6)
fruits.enqueue('Apple')
fruits.enqueue('Banana')
fruits.enqueue('Mango')
fruits.enqueue('Guava')
fruits.enqueue('Orange')
fruits.enqueue('Papaya')
print(fruits)
print(rearrange_fruits(fruits))
"""

"""
inarr1 = ['QW', 'RN', 'KOI', 'POL', 'ERT', 'XCV', 'ERB', 'LHJ', 'AS']
inrow = 3
incol = 3
inarr2 = [31, 23, 21, 11, 33, 13, 12, 22, 32]
inkey = 'CARZ'
strmatrix = []
# strmatrix = [[''] * inrow] * incol
k = 0
for i in range(incol):
    a = []
    for j in range(incol):
        a.append(k)
        k += 1
    strmatrix.append(a)
print(strmatrix)

# for location in inarr2:
#     data = inarr1[inarr2.index(location)]
#     row = location // 10 - 1
#     col = location % 10 - 1
#     for i in range(incol):
#         if i == col:
#             for j in range(inrow):
#                 if j == row:
#                     strmatrix[row][col] = data

# for i in range(incol):
#     for j in range(incol):
#         print(strmatrix[i][j], end="\t")
#     print()
# print(strmatrix)
"""

"""
class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if self.__top == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__top == -1:
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("The stack is full!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is empty!!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index])
                index -= 1

    def get_top(self):
        return self.__top

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__top
        while index >= 0:
            msg.append(str(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg


class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index])

    def get_front(self):
        return self.__front

    def get_rear(self):
        return self.__rear

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while index <= self.__rear:
            msg.append(str(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg


def fun(input_stack):
    output_queue = Queue(input_stack.get_max_size())
    temp_queue = Queue(input_stack.get_max_size())
    while not input_stack.is_empty():
        data = input_stack.pop()
        if data % 2 == 0:
            output_queue.enqueue(data)
        else:
            temp_queue.enqueue(data)
    temp_data = 0
    while not temp_queue.is_empty():
        temp_data += temp_queue.dequeue()
        output_queue.enqueue(temp_data)
    output_queue.display()


def fun2(input_stack):
    num = input_stack.get_max_size() - 1
    num1 = 1
    while num > 0:
        top_element = input_stack.pop()
        temp_stack = Stack(input_stack.get_max_size())
        num2 = 1
        while num2 <= num1:
            element = input_stack.pop()
            temp_stack.push(element + top_element)
            num2 += 1
        while not temp_stack.is_empty():
            input_stack.push(temp_stack.pop())
        input_stack.push(top_element)
        num1 += 1
        num -= 1
    return input_stack


sample = Stack(5)
sample.push(1)
sample.push(2)
sample.push(3)
sample.push(4)
sample.push(5)
print(fun2(sample))
"""

"""
#   Bubble sort no of passes
def swap(num_list, first_index, second_index):
    global no_of_swaps
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]
    no_of_swaps += 1


def bubble_sort(num_list):
    global no_of_passes
    end_index = len(num_list)
    for index1 in range(end_index):
        swapped = False
        for index2 in range(0, (end_index - index1 - 1)):
            if num_list[index2] > num_list[index2 + 1]:
                swap(num_list, index2, index2 + 1)
                swapped = True
        if not swapped:
            break
        no_of_passes += 1
        print("At the end of pass-", no_of_passes, ":", num_list)


no_of_swaps = 0
no_of_passes = 0
# num_list = [89, 43, 99, 55, 87, 67]
num_list = [67, 34, 8, 22, 23]
# num_list = [5, 4, 3, 2, 1]
# num_list = [32, 21, 1, 34, 97, 46, 67, 56]
print("In the beginning:", num_list)
print("______________________________________________")
bubble_sort(num_list)
print("______________________________________________")
print("At the end:", num_list)
print("______________________________________________")
print("No. of swaps:", no_of_swaps)
print("No. of passes:", no_of_passes)

"""
"""
inarr = ['trees', 'of', 'apples']
count_inarr = []
tempstr = ''
innum = 1
innum2 = 2
for item in inarr:
    foo = []
    count = 1
    for letter in item:
        if letter not in foo:
            foo.append(letter)
        else:
            count += 1
    count_inarr.append(count)
i = 1
for i in range(1, len(inarr)):
    element = inarr[i]
    ch = element[count_inarr[i - 1] % len(element)]
    tempstr += ch

res = [tempstr[i: j] for i in range(len(tempstr))
       for j in range(i + 1, len(tempstr) + 1)]
outstr = len(res)
print(outstr)
"""


