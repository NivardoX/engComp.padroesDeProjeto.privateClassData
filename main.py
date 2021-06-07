class DataClass:
    """
    Hide all the attributes.
    """

    def __init__(self):
        print("Criando dataclass")
        self.value = None

    def __get__(self, instance, owner):
        print("Pegando o valor de dentro da dataclass")
        return self.value

    def __set__(self, instance, value):
        if self.value is None:
            print("Settando o valor a dentro da dataclass")
            self.value = value


class MainClass:
    """
    Initialize data class through the data class's constructor.
    """

    attribute = DataClass()

    def __init__(self, value):
        print("Criando MainClass")

        self.attribute = value


def main():
    m = MainClass(True)
    m.attribute = False
    print(m.attribute)

if __name__ == "__main__":
    main()
