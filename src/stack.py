class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.stack_list = []
        self.top = None
        self.size = 0

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        # if self.top:
        #     new_node.next_node = self.top
        self.top = new_node
        self.stack_list.append(new_node)
        self.size += 1

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        self.top = self.top.next_node
        last_del = self.stack_list.pop()
        self.size -= 1
        return last_del.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        data_list = []
        for item in self.stack_list:
            data_list.append(item.data)
        return "\n".join(data_list)
