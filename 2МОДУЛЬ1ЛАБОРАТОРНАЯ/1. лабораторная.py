import doctest


class Student:
    def __init__(self, name: str, age: int, course_number: int):
        """
        :param name: имя фамилия
        :param age: возраст
        :param course_number: номер курса

        Примеры:
        >>> student = Student("Вася Пупкин", 20, 4)
        """
        self.name = name
        self.age = age
        self.course_number = course_number
        if not isinstance(name, str):
            raise TypeError("Имя и фамилия должны быть типа str")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if course_number < 1 or course_number > 6:
            raise ValueError("Номер курса должен быть от 1 до 6.")

    def increase_age(self, years: int) -> None:
        """
        Увеличивает возраст студента на указанное количество лет.
        :years (int): количество лет, на которое нужно увеличить возраст студента

        Примеры:
        >>> student = Student("Вася Пупкин", 20, 4)
        >>> student.increase_age(5)
        >>> student.age
        25
        >>> student.increase_age(-3) #специально показана ошибка через doctest
        """
        if not isinstance(years, int):
            raise TypeError("Добавляемые года должен быть типа int")
        if years < 0:
            raise ValueError("Добавленные года должны быть положительным числом")

        self.age += years

    def change_name(self, new_name: str) -> None:
        """
        Изменяет имя студента.
        :param new_name: новое имя студента

        Примеры:
        >>> student = Student("Вася Пупкин", 20, 4)
        >>> student.change_name("Петя Пупкин")
        >>> student.name
        'Петя Пупкин'
        >>> student.change_name(123) #специально показана ошибка через doctest
        """
        if not isinstance(new_name, str):
            raise TypeError("Имя и фамилия должны быть типа str")

        self.name = new_name


class Teapot:
    def __init__(self, max_capacity: float, temperature: float):
        """
        :param max_capacity: максимальный объем воды, который может вместить чайник (в литрах)
        :param temperature: температура воды в чайнике (в градусах Цельсия)

        Примеры:
        >>> teapot = Teapot(1.5, 20)
        """
        self.max_capacity = max_capacity
        self.temperature = temperature
        if not isinstance(max_capacity, (int, float)):
            raise TypeError("Максимальный объем должен быть числом")
        if max_capacity <= 0:
            raise ValueError("Максимальный объем должен быть положительным числом")
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")

    def fill_water(self, amount: float) -> None:
        """
        Добавляет указанное количество воды в чайник.
        :param amount: количество воды, которое нужно налить (в литрах)

        Примеры:
        >>> teapot = Teapot(1.5, 20)
        >>> teapot.fill_water(0.5)
        >>> teapot.max_capacity
        1.0
        >>> teapot.fill_water(-0.3) #специально показана ошибка через doctest
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество воды должно быть числом")
        if amount <= 0:
            raise ValueError("Количество воды должно быть положительным числом")
        if self.max_capacity - amount < 0:
            raise ValueError("Чайник не может вместить указанное количество воды")

        self.max_capacity -= amount

    def play_sound_signal(self) -> None:
        """
        Воспроизводит звуковой сигнал, если температура воды достигла 100 градусов Цельсия.

        Примеры:
        >>> teapot = Teapot(1.5, 20)
        >>> teapot.temperature = 95
        >>> teapot.play_sound_signal()
        >>> teapot.temperature = 100
        >>> teapot.play_sound_signal()
        Звуковой сигнал
        >>> teapot.temperature = 105
        >>> teapot.play_sound_signal()
        Звуковой сигнал
        """
        if self.temperature >= 100:
            print("Звуковой сигнал")


class Printer:
    def __init__(self, printer_model: str, cartridge_level: int, max_paper: int):
        """
        :param printer_model: модель принтера
        :param cartridge_level: уровень заправки катриджа в процентах
        :param max_paper: максимальное количество листов, которое можно положить внутрь

        Примеры:
        >>> printer = Printer("HP LaserJet", 50, 100)
        """
        self.printer_model = printer_model
        self.cartridge_level = cartridge_level
        self.max_paper = max_paper
        if not isinstance(printer_model, str):
            raise TypeError("Модель принтера должна быть типа str")
        if cartridge_level < 0 or cartridge_level > 100:
            raise ValueError("Уровень заправки катриджа должен быть от 0 до 100")
        if max_paper <= 0:
            raise ValueError("Максимальное количество листов должно быть положительным числом")

    def low_cartridge_notification(self) -> bool:
        """
        Проверяет уровень заправки катриджа и возвращает True, если он меньше 10%, иначе False.

        Примеры:
        >>> printer = Printer("HP LaserJet", 50, 100)
        >>> printer.low_cartridge_notification(50)
        False
        >>> printer.cartridge_level = 5
        >>> printer.low_cartridge_notification()
        True
        """
        if self.cartridge_level < 10:
            return True
        else:
            return False

    def add_paper(self, sheets: int) -> None:
        """
        Показывает количество листов, которые еще может вместить в себя принтер
        :param sheets: количество листов, которое добавляется

        Примеры:
        >>> printer = Printer("HP LaserJet", 50, 100)
        >>> printer.add_paper(20)
        80
        >>> printer.add_paper(-5) #специально показана ошибка через doctest
        """
        if not isinstance(sheets, int):
            raise TypeError("Количество листов должно быть типа int")
        if sheets <= 0:
            raise ValueError("Количество листов должно быть положительным числом")

        self.max_paper -= sheets
        return self.max_paper


if __name__ == "__main__":
    doctest.testmod()
