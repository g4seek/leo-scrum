class Task:
    def __init__(self, id, name, priority, status, link):
        self.id = id
        self.name = name
        self.priority = priority
        self.status = status
        self.link = link

    def __str__(self):
        return "id:" + str(self.id) + ",name:" + self.name + ",priority:" + self.priority + ",status:" + self.status + ",link:" + self.link


if __name__ == '__main__':
    task = Task('1', 'a', '3', 'start', 'a')
    print task
    pass