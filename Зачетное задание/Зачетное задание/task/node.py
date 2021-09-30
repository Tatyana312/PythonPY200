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

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), cls)):
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

if __name__ == '__main__':
    node_1 = DoubleLinkedNode(1)
    node_2 = DoubleLinkedNode(2)
    node_3 = DoubleLinkedNode(3)

