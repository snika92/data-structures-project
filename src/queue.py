class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.queue = []
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if len(self.queue) > 0:
            self.queue[-1].next_node = new_node
        self.queue.append(new_node)
        self.size += 1
        self.head = self.queue[0]
        self.tail = self.queue[-1]

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        data_list = []
        for item in self.queue:
            data_list.append(item.data)
        return "\n".join(data_list)
