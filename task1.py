
class Product:

    """Класс, содержащий информацию о товаре."""

    def __init__(self, _name: str = "Без названия", _code: str = "000", _quantity: int = 1) -> None:

        """Метод инициализации объекта класса.

        Args:
            name: наименование товара
            code: шифр товара
            quantity: количество товара
        """
        self.set_name(_name)
        self.set_code(_code)
        self.set_quantity(_quantity)


    def set_name(self, name: str) -> None:

        """Сеттер названия товара.

        Args:
            name: название товара
        """

        if name:
            self._name = name
        else:

            print("Имя не должно быть пустой строкой!\n")


    def get_name(self) -> str:

        """Геттер названия товара.

        Returns:
            str: название товара
        """

        return self._name


    def set_code(self, code: str) -> None:

        """Сеттер шифра товара.

        Args:
            code: шифр товара
        """
        if code:
            self._code = code
        else:

            print("Шифр не должен быть пустой строкой!\n")


    def get_code(self) -> str:

        """Геттер шифра товара.

        Returns:
            str: шифр товара
        """

        return self._code


    def set_quantity(self, quantity: int) -> None:

        """Сеттер количества товара.

        Args:
            quantity: количество товара
        """

        if not isinstance(quantity, int) or quantity < 0:

            print("Количество должно быть натуральным числом!\n")

        else:
             self._quantity = quantity


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
            f'Шифр товара: {self.get_code()}\n'
            f'Количество товара: {self.get_quantity()}\n'
        )


    def add_product(self, quantity: int) -> None:

        """Функция увеличения количества товара.

        Args:
            quantity: количество товара (целое число > 0)
        """

        if not isinstance(quantity, int) or quantity < 0:

                print("Прибавка должна быть целым неотрицательным числом!\n")

        else:

            self._quantity += quantity


    def remove_product(self, quantity: int) -> None:

        """Функция уменьшения количества товара.

        Args:
            quantity: количество товара
        """

        if not isinstance(quantity, int) or quantity < 0:

            print("Убавка должна быть целым неотрицательным числом!\n")

        elif (self._quantity - quantity) < 0:

            print('У вас слишком мало товара!\n')

        else:
            self._quantity -= quantity



class Menu:

    """Класс для взаимодействия с пользователем через консольное меню."""

    def __init__(self, product: Product) -> None:

        """Инициализация меню.

        Args:
            product: объект товара, с которым будет работать меню
        """

        self._product = product


    def show_menu(self) -> None:

        """Вывод пунктов меню на экран."""

        print(
            "МЕНЮ:\n"
            "  1. Показать товар\n"
            "  2. Изменить наименование\n"
            "  3. Изменить шифр\n"
            "  4. Изменить количество\n"
            "  5. Прибавить количество\n"
            "  6. Списать количество\n"
            "  0. Выход"
        )


    def run(self) -> None:

        """Основной цикл работы меню. Выход по команде '0'."""

        end = False
        choice = ""

        while not end:

            self.show_menu()
            choice = input("Выберите действие: ").strip()

            match choice:
                case "0":
                    print("Работа завершена. До свидания!")
                    end = True
                case "1":
                    self._product.show_info()
                case "2":
                    self._product.set_name(input("  Новое наименование: "))
                case "3":
                    self._product.set_code(input("  Новый шифр: "))
                case "4":
                    self._product.set_quantity(int(input("  Новое количество (>0): ")))
                case "5":
                    self._product.add_product(int(input("  Сколько прибавить: ")))
                case "6":
                    self._product.remove_product(int(input("  На сколько уменьшить: ")))
                case _:

                    print("  Нет такого пункта, попробуйте снова.\n")



product1 = Product()
product1.set_name('Плюшевый кот')
product1.set_code('R2-D2')
product1.set_quantity(999)
product1.show_info()
product1.remove_product(1000)
product1.remove_product(67)
product1.show_info()

my_product = Product("Ноутбук", "NB-001", 3)
my_menu = Menu(my_product)
my_menu.run()

