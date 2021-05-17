class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class SortedLinkedList:
    def __init__(self, list_type):
        self.__head = None
        self.__list_size = 0
        self.__list_type = list_type

    def add_item(self, data):
        if not isinstance(data, self.__list_type):
            raise TypeError(f"Type of added item must be {self.__list_type}")
        elif self.__head is None:
            node = Node(data=data)
            self.__head = node
            self.__list_size += 1
        elif self.__head.data > data:
            node = Node(data=data)
            node.next = self.__head
            self.__head = node
            self.__list_size += 1
        else:
            current_node = self.__head
            while current_node.next is not None:
                if current_node.next.data > data:
                    node = Node(data=data)
                    node.next = current_node.next
                    current_node.next = node
                    self.__list_size += 1
                    return
                current_node = current_node.next
            node = Node(data=data)
            node.next = current_node.next
            current_node.next = node
            self.__list_size += 1
            return

    def is_empty(self):
        return not self.__list_size

    def clear(self):
        self.__head = None
        self.__list_size = 0

    def remove(self, item):
        previous_node = None
        current_node = self.__head
        while current_node is not None:
            if current_node.data == item:
                if previous_node is not None:
                    previous_node.next = current_node.next
                    self.__list_size -= 1
                    return
                self.__head = current_node.next
                self.__list_size -= 1
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError("SortedLinkedList.remove(item): item not in SortedLinkedList")

    def index(self, item):
        current_node = self.__head
        counter = 0
        while current_node is not None:
            if current_node.data == item:
                return counter
            counter += 1
            current_node = current_node.next
        raise ValueError("SortedLinkedList.index(item): item not in SortedLinkedList")

    def count(self, item):
        current_node = self.__head
        counter = 0
        while current_node is not None:
            if current_node.data == item:
                counter += 1
            current_node = current_node.next
        return counter

    def pop(self, index):
        if index - 1 > self.__list_size:
            raise IndexError("pop index out of range")
        if index == 0:
            node = self.__head
            self.__head = self.__head.next
            return node
        else:
            previous_node = self.__head
            node = self.__head.next
            for _ in range(index - 1):
                node = node.next
                previous_node = previous_node.next
            previous_node.next = node.next
            return node

    def copy_duplicate(self):
        current_node = self.__head
        previous_node_data = None
        while current_node is not None:
            next_node = current_node.next
            next_node_data = next_node.data if next_node is not None else ""
            if current_node.data != next_node_data and previous_node_data != current_node.data:
                duplicated_node = Node(current_node.data)
                current_node.next = duplicated_node
                duplicated_node.next = next_node
                previous_node_data = duplicated_node.data
                current_node = next_node
            else:
                previous_node_data = current_node.data
                current_node = current_node.next
        return

    def extend(self, items):
        for item in items:
            self.add_item(item)

    def __str__(self):
        str_representation = ""
        current_node = self.__head
        while current_node is not None:
            str_representation += str(current_node.data)
            current_node = current_node.next
            if current_node is None:
                break
            str_representation += ", "
        str_representation = f'[{str_representation}]'
        return str_representation

    def sum(self):
        return self.__sum(self.__head)

    def __sum(self, current):
        if current.next is None:
            return current.data
        else:
            return current.data + self.__sum(current.next)

    def print(self):
        print(self.__print(self.__head))

    def __print(self, current):
        if current.next is None:
            return str(current.data)
        else:
            return str(current.data) + " " + self.__print(current.next)

    def reverse_print(self):
        self.__reverse_print(self.__head)
        print()

    def __reverse_print(self, current):
        if current.next:
            self.__reverse_print(current.next)
        print(current.data, end=" ")

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.__list_size

    def __iter__(self):
        current_node = self.__head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    def __bool__(self):
        return self.__head is not None
