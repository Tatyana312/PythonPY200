from typing import Iterable, Optional

from node import Node

class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.list_nodes = []
        if data is not None:
            self.init_linked_list(data)

    def init_linked_list(self, data: Iterable):
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        self.list_nodes = [Node(value) for value in data]

        # TODO составьте алгоритм, который свяжет узлы
        for i in range(0, len(self.list_nodes)-1): # последнй элемент несчем сравнивать
            left_node = self.list_nodes[i]
            right_node = self.list_nodes[i+1]
            self.list_nodes(left_node,right_node)

    # TODO каким должен быть этот метод? - декоратор метод к атрибутам класса или методам класа. Зависит от внутреннего предсиавоения (списка) -нет self cls - не зависит
    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.
        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def __str__(self) -> str:
        return str(self.list_nodes)

if __name__ == "__main__":
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)
