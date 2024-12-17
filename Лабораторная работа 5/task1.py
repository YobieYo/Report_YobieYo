import doctest

                    # TODO Написать 3 класса с документацией и аннотацией типов
class List:
    """
    Документация на класс
    Класс описывает модель листа бумаги
    """
    def __init__(self, capacity_area: float, occupied_area: float):
        """
         Создание и подготовка объекта лист

        :param capacity_area: Площадь листа.
        :param occupied_area: Занятая площадь листа.
        """
        if not isinstance(capacity_area,(int, float)):
            raise TypeError("Неправильный тип атрибута")
        if capacity_area <=0:
            raise ValueError("Атрибут не может быть отрицательным или равен нулю")
        self.capacity_area = capacity_area
        if not isinstance(occupied_area,(int, float)):
            raise TypeError("Неправильный тип атрибута")
        if occupied_area < 0:
            raise ValueError("Атрибут не может быть отрицательным")
        self.occupied_area = occupied_area
    def is_clear_list(self) -> bool:
        """
        Функция которая проверяет является ли лист чистым

        :return: Является ли лист чистым

        Примеры:
        >>> list = List(500, 0)
        >>> list.is_clear_list()
        """
        ...
    def write_on_list(self,writing:float) -> None:
        """
                Метод, который пишет что-то на листе

                :param writing: Площадь написанного текста

                :raise ValueError: Если площадь написанного текста больше оставшегося места на листе

                Примеры:
                >>> list = List(500, 0)
                >>> list.write_on_list(20)
                """
        if not isinstance(writing,(int,float)):
            raise TypeError("Неправильный тип аргумента")
        if writing < 0:
            raise ValueError("Аргумент не может быть отрицательным")
        ...
class Wallet:
    """
    Класс описывает модель кошелька.
    """
    def __init__(self, owner: str, currency: str, balance: float = 0.0):
        """
        Создание и подготовка объекта кошелек

        :param owner: Имя владельца кошелька.
        :param currency: Валюта кошелька (например, "USD", "EUR", "RUB").
        :param balance: Начальный баланс кошелька (по умолчанию 0.0).

        :raise TypeError: Если `owner` или `currency` не являются строками или `balance` не является числом.
        :raise ValueError: Если `currency` - пустая строка, или если `balance` является отрицательным числом.
        """
        if not isinstance(owner, str):
            raise TypeError("Имя владельца кошелька должно быть строкой.")
        self.owner = owner

        if not isinstance(currency, str):
            raise TypeError("Валюта должна быть строкой.")
        if not currency:
            raise ValueError("Валюта не может быть пустой строкой.")
        self.currency = currency

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом.")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным числом.")
        self.balance = balance

    def add_money(self, amount: float) -> None:
        """
        Метод для добавления денег в кошелек.

        :param amount: Сумма для добавления в кошелек.

        :raise TypeError: если amount не число
        :raise ValueError: Если `amount` не является положительным числом.

        Примеры:
        >>> wallet = Wallet("Анна", "USD", 50.0)
        >>> wallet.add_money(25.0)
        """
        if not isinstance(amount, (int, float)):
             raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма для добавления должна быть положительной.")
        ...


    def spend_money(self, amount: float) -> None:
        """
        Метод для траты денег из кошелька.

        :param amount: Сумма для траты из кошелька.

         :raise TypeError: если amount не число
        :raise ValueError: Если `amount` не является положительным числом, или если `amount` превышает текущий баланс.

        Примеры:
        >>> wallet = Wallet("Анна", "USD", 50.0)
        >>> wallet.spend_money(10.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма для траты должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Сумма для траты превышает текущий баланс.")
        ...

    def get_balance(self) -> float:
      """
      Метод возвращает текущий баланс кошелька.

      :return: текущий баланс.

      Примеры:
      >>> wallet = Wallet("Анна", "USD", 50.0)
      >>> wallet.get_balance()
      """
      ...

class Tree:
    """
    Класс описывает модель дерева.
    """
    def __init__(self, species: str, height: float, age: int = 0):
        """
        Подготовка объекта дерево.

        :param species: Вид дерева (например, "Дуб", "Береза", "Сосна").
        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах (по умолчанию 0).

        :raise TypeError: Если `species` не является строкой, или если `height` не является числом, или если `age` не является целым числом.
        :raise ValueError: Если `species` - пустая строка, или если `height` или `age` являются отрицательными числами.
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not species:
            raise ValueError("Вид дерева не может быть пустой строкой.")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом.")
        if height < 0:
            raise ValueError("Высота не может быть отрицательным числом.")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом.")
        self.age = age

    def grow(self, years: int, height_increase: float) -> None:
        """
        Метод для моделирования роста дерева.

        :param years: Количество лет, на которое выросло дерево.
        :param height_increase: Увеличение высоты дерева в метрах.

        :raise TypeError: Если `years` не является целым числом, или если `height_increase` не является числом.
        :raise ValueError: Если `years` или `height_increase` являются отрицательными числами.

        Примеры:
        >>> tree = Tree("Береза", 5.0, 10)
        >>> tree.grow(2, 1.0)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом.")
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным числом.")
        if not isinstance(height_increase, (int, float)):
            raise TypeError("Увеличение высоты должно быть числом.")
        if height_increase < 0:
              raise ValueError("Увеличение высоты не может быть отрицательным числом.")
        ...

    def get_height(self) -> float:
        """
        Метод для получения текущей высоты дерева.
        :return: Высота дерева в метрах.

        Примеры:
        >>> tree = Tree("Дуб", 10.0)
        >>> tree.get_height()
        """
        ...
    def get_age(self) -> int:
        """
        Метод для получения текущего возраста дерева.
         :return: Возраст дерева в годах

         Примеры:
         >>> tree = Tree("Сосна", 7.0, 20)
         >>> tree.get_age()
        """
        ...
if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
