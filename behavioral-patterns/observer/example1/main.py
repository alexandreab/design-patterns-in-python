from observer import Subject, Observer

class Tamagoshi(Subject):
    def __init__(self):
        super(Tamagoshi, self).__init__()
        self._life = 100

    @property
    def life(self):
        return self._life

    @property
    def is_alive(self):
        return self.life > 0

    def next_tick(self):
        if self.life <= 0:
            return

        self._life -= 10
        print(f"Life reduced to {self._life}");
        self.notify_observers()


class StatusReporter(Observer):

    def notify(self, subject: Subject):
        if subject.life > 80:
            print("Tamagoshi is very healthy");
        elif subject.life > 50:
            print("Tamagoshi is normal");
        elif subject.life > 20:
            print("Tamagoshi needs attention");
        elif subject.life > 0:
            print("Tamagoshi needs attention urgently!");
        else:
            print("Tamagoshi died. :'( F");




if __name__ == '__main__':
    tamagoshi = Tamagoshi()
    reporter = StatusReporter(tamagoshi)
    while tamagoshi.is_alive:
        tamagoshi.next_tick()
