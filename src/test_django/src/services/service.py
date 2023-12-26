from src.interfaces import IRepository


class Service:
    def __init__(self, repository1: IRepository, repository2: IRepository):
        self.repository1 = repository1
        self.repository2 = repository2

    def say_hello(self):
        h1 = self.repository1.say_hello()
        h2 = self.repository2.say_hello()
        return f"{h1}, {h2}"
