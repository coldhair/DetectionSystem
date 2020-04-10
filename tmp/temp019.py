class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('{} 正在玩飞行棋。'.format(self._name))
        else:
            print('{} 正在玩斗地主。'.format(self._name))


def main():
    person = Person('吕艳朋', 36)
    person.play()
    person.age = 14
    person.play()


if __name__ == '__main__':
    main()
