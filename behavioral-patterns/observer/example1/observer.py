class Subject:
    def __init__(self):
        self.observers = list()

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.notify(self)


class Observer:
    def __init__(self, subject: Subject):
        subject.add_observer(self)

    def notify(self, subject: Subject):
        raise NotImplementedError("State base class can not be instantiated")

