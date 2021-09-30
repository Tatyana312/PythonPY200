from collections.abc import MutableSequence

from node import Node

class LinkedList(MutableSequence):

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:
            raise IndexError()
        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)
        self.len -= 1

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()
        insert_node = Node(value)
        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.len += 1
        elif index >= self.len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)
            self.len += 1

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node
        self.len += 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), self.__class__)):
            raise TypeError

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head: Optional["self.__class__"]):
        # print("Вызван setter1")
        self.is_valid(head)
        self.__head = head

    @property
    def tail(self):
        return self.__tail

    @property
    def tail(self):
        return self.tail

    @tail.setter
    def tail(self, tail: Optional["self.__class__"]):
        self.is_valid(tail)
        self.tail = tail

class DoubleLinkedList(LinkedList):

    def __init__(self, data: Iterable = None):
        """Конструктор двусвязного списка"""
        super().__init__(len)

        if data is not None:
            for value in data:
                self.append(value)

    def double_append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.double_linked_nodes(self.tail, append_node, self.tail.prev)
            self.tail = append_node
            self.tail.next.prev = append_node

        self.len += 1

    def double_step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.tail
        for _ in range(index):
            current_node = current_node.prev

        for _ in reversed(self.len):
            current_node = current_node.prev

        return current_node

    @staticmethod
    def double_linked_nodes(left_node: Optional[DoubleLinkedNode] = None, right_node: Optional[DoubleLinkedNode] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """

        left_node.next = right_node
        right_node.prev = left_node
        right_node.next.prev = right_node
        left_node.next.prev = left_node

    def to_list(self) -> list:
        return [double_linked_list_value for double_linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index: int, value: Any):

        new_node = Node(data=new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        new_node = Node(data=new_data)


        new_node.next = prev_node.next


        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

        new_node = Node(data=new_data)
        last = self.head

        # 3. This new node is going to be the
        # last node, so make next of it as NULL
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return


        while (last.next is not None):
            last = last.next

        last.next = new_node

        new_node.prev = last

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:
            raise IndexError()
        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)
        self.len -= 1

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:
            raise IndexError()

        if index == 0:
            self.head = self.head.next

        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None

        else:
            self.tail.prev = self.step_by_step_on_nodes(index - 1)
            del_node = tail.prev.next = tail.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)
        self.len -= 1



        if dele.next is not None:
            dele.next.prev = dele.prev


        if dele.prev is not None:
            dele.prev.next = dele.next

        gc.collect()

if __name__ == "__main__":
    ...
