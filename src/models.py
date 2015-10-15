class Task:
    def __init__(self, name, priority, status, link):
        self.name = name
        self.priority = priority
        self.status = status
        self.link = link


class Module:
    def __init__(self, title, memo, image):
        self.title = title
        self.memo = memo
        self.image = image
