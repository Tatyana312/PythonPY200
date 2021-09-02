class Glass:
    def __init__(self, capacity_volume: [int, float], occupied_volume: [int, float]):

        #  TODO ициализировать объект "Стакан"
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, (int, float)):
            raise TapeError
        if occupied_volume < 0:
            raise ValueError

        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    # TODO инициализировать два объекта типа Glass
    glass_1 = Glass(500, 0)


    # TODO попробовать инициализировать не корректные объекты
