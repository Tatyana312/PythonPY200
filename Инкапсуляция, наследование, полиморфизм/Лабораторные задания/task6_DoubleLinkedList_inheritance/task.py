from typing import Any, Iterable, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), self.__class__)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):

    def __init__(self, value: Any, next_: Optional["DoubleLinkedNode"] = None, prev: Optional["Node"] = None):
        """
        Создаем новый узел для двусвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        :param prev: предыдущий узел, если он есть
        """
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        if self.next is None:
            i = f"DoubleLinkedNode({self.value}, {None}, DoubleLinkedNode({self.prev}))"
        elif self.prev is None:
            i = f"DoubleLinkedNode({self.value}, DoubleLinkedNode({self.next}), {None})"
        else:
            i = f"DoubleLinkedNode({self.value}, DoubleLinkedNode({self.next}), " \
                 f"DoubleLinkedNode({self.prev}))"
        return i

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"] = None) -> None:
        self.is_valid(prev)
        self._prev = prev

class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node
        self.len += 1

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

    @staticmethod
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

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    # TODO реализовать getter и setter для head

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

      # TODO реализовать getter и setter для tail
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

    # TODO Реализовать класс DoubleLinkedList


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

if __name__ == "__main__":

    list_ = [1, 2, 3, 4]

    ll = DoubleLinkedList(list_)
    print(ll.head)
    print(ll.tail)

    print(repr(no)