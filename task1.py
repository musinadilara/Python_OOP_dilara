
class Product:

    """Класс, содержащий информацию о товаре."""

    def __init__(self, name: str, sipher: str, quantity: int, ) -> None:

        """Метод инициализации объекта класса.

        Args:
            name: наименование товара
            sipher: шифр товара
            quantity: количество товара
        """
        self.set_name(name)
        self.set_sipher(sipher)
        self.set_quantity(quantity)


    def set_name(self, name: str) -> None:

        """Сеттер названия товара.

        Args:
            name: название товара
        """

        self._name = name


    def get_name(self) -> str:

        """Геттер названия товара.

        Returns:
            str: название товара
        """

        return self._name


    def set_sipher(self, sipher: str) -> None:

        """Сеттер шифра товара.

        Args:
            sipher: шифр товара
        """

        self._sipher = sipher


    def get_sipher(self) -> str:

        """Геттер шифра товара.

        Returns:
            str: шифр товара
        """

        return self._sipher


    def set_quantity(self, quantity: int) -> None:

        """Сеттер количества товара.

        Args:
            quantity: количество товара
        """

        if not isinstance(quantity, int):

            raise ValueError("Количество должно быть целым числом")

        if quantity < 0:

            raise ValueError("Количество должно быть неотрицательным числом")

        self._quantity = quantity

        print('  Количество товара изменилось')


    def get_quantity(self) -> int:

        """Геттер количества товара.

        Returns:
            int: количество товара
        """

        return self._quantity


    def show_info(self):

        """Вывод информации о товаре."""

        print(
            f'Название товара: {self.get_name()}\n'
            f'Шифр товара: {self.get_sipher()}\n'
            f'Количество товара: {self.get_quantity()}\n'
        )


    def __str__(self):

        """Вывод информации о товаре автоматически через print(экземпляр класса)."""

        return f"Товар '{self._name}' шифр ({self._sipher}), количество: {self._quantity}."


    def add_product(self, quantity: int) -> None:

        """Функция увеличения количества товара.

        Args:
            quantity: количество товара (целое число > 0)

        Raises:
            ValueError: если quantity не целое или <= 0
        """
        if not isinstance(quantity, int):

            raise ValueError("Прибавка должна быть целым числом")

        if quantity <= 0:

            raise ValueError("Прибавка должна быть > 0")

        self._quantity += quantity

        print(f'  Количество увеличилось на {quantity}')


    def remove_product(self, quantity: int) -> None:

        """Функция уменьшения количества товара.

        Args:
            quantity: количество товара
        """

        if (self._quantity - quantity) >= 0:

            self._quantity -= quantity
        else:

            print('У вас слишком мало товара!')

        print(f'  Количество уменьшилось на {quantity}')


    def is_available(self):

        """Функция проверки наличия товара.

        Returns:
            boll: ответ на вопрос о наличии товара
        """

        return self._quantity > 0


    def menu(self):

        """Меню для работы с товаром.

        Показывает список действий, запрашивает выбор пользователя
        и выполняет соответствующее действие над текущим объектом.
        Работает до ввода команды "0" (выход).
        """

        choice = ""
        while choice != "0":

            print("МЕНЮ:\n"
                "  1. Показать товар\n"
                "  2. Изменить наименование\n"
                "  3. Изменить шифр\n"
                "  4. Изменить количество\n"
                "  5. Прибавить количество\n"
                "  6. Списать количество\n"
                "  7. Проверить наличие\n"
                "  0. Выход"
            )

            choice = input("Выберите действие: ").strip()

            try:

                if choice == "1":

                    self.show_info()

                elif choice == "2":

                    self.set_name(input("  Новое наименование: "))

                    print('  Название товара изменилось.\n')

                elif choice == "3":

                    self.set_sipher(input("  Новый шифр: "))

                    print('  Шифр был изменен.\n')

                elif choice == "4":

                    self.set_quantity(int(input("  Новое количество (>0): ")))

                elif choice == "5":

                    self.add_product(int(input("  Сколько прибавить: ")))

                elif choice == "6":

                    self.remove_product(int(input("  На сколько уменьшить: ")))

                elif choice == "7":

                    print(f"  В наличии: {'да' if self.is_available() else 'нет'}\n")

                elif choice != "0":

                    print("Нет такого пункта, попробуйте снова.")

            except ValueError as e:
                print(f"  Ошибка: {e}")

        print("Работа завершена. До свидания!")




if __name__ == "__main__":
    product = Product("Ноутбук", "NB-001", 3)
    product.menu()

'''
    p2.show_info()

    print(p2.get_name(), p2.get_sipher(), p2.get_quantity())
    print(p2)

    p2.set_quantity(15)
    p2.show_info()

    try:

        p2.set_quantity(-5)

    except ValueError as e:

        print("Ошибка:", e)

'''