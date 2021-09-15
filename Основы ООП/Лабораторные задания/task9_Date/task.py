# TODO class Date
class Date:
    def __init__(self, DD: int, MM: int, YYYY: int):
        if not isinstance(self.DD, int):
            raise TypeError
        self.DD = DD
        if not isinstance(self.MM, int):
            raise TypeError
        self.MM = MM
        if not isinstance(self.YYYY, int):
            raise TypeError
        self.YYYY = YYYY

    def get_DD(self):
        return self.DD

    def get_MM(self):
        return self.MM

    def get_YYYY(self):
        return self.YYYY

    def __repr__(self):
        return f"Date({self.DD}, {self.MM}, {self.YYYY})"

    def __str__(self):
        return f"{self.DD}/{self.MM}/{self.YYYY}"


if __name__ == "__main__":
    date = Date(13, 9, 2021)  # экземпляр класса
    print(date)