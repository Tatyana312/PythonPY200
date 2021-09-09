# TODO class Date
class Date:
    def __init__(self, DD: int, MM: int, YYYY: int):
        self.DD = DD
        self.MM = MM
        self.YYYY = YYYY

    TypeError int

    def __repr__ (self):
        return f"Date({self.DD}, {self.MM}, {self.YYYY})"

    def __str__(self):
        return f"{self.DD}/{self.MM}/{self.YYYY}"

