from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        self.next = None
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.next = next_


def linked_nodes(left_node: Node, right_node: Optional["Node"] = None) -> None:
    """
    Функция, которая связывает между собой два узла.

    :param left_node: Левый или предыдущий узел
    :param right_node: Правый или следующий узел
    """
    # self.left_node = left_node
    # self.right_node = right_node
    # return self.linked_nodes = (left_node,right_node)
    left_node.set_next(right_node)
    # TODO реализовать функцию, принять левый узел два узла левый и правый связать между собой


if __name__ == '__main__':
    ...  #
    node_1=Node(1)
    node_2 = Node(2)
    Node.set_next(node_1, node_2)

    print(node_1)

    # TODO самостоятельно проверьте работоспособность  функции linked_nodes
