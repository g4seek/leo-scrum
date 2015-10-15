class Task:
    def __init__(self, id, name, priority, status, link):
        self.id = id
        self.name = name
        self.priority = priority
        self.status = status
        self.link = link


class Module:
    def __init__(self, id, title, memo, image):
        self.id = id
        self.title = title
        self.memo = memo
        self.image = image
