class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""
        if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 400 == 0) and (year % 100 == 0)):
            print("Год {self.year} - високосный")
        else: print("Год {self.year} - не високосный")
        return True


    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        index = month-1
        if  self.is_leap_year(year) == True:
            max_day = self.DAY_OF_MONTH[1][index]
        else: max_day = self.DAY_OF_MONTH[0][index]
        return max_day

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if 12 < self.month < 1:
            raise TimeoutError
        if 9999 < self.year < 1:
            raise TimeoutError
        if 31 < self.day < 1:
            raise TimeoutError



if __name__ == "__main__":
    # Write your solution here
    pass
