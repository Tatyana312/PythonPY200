# TODO  создать класс Glass
class Glass():
    def __init__(self, capacity_volume: int, occupied_volume: int):
        self.capacity_volume = capacity_volume
        #get_capacity_volume()
        self.occupied_volume = occupied_volume
        #get_occupied_volume()

    def get_capacity_volume(self):
        return self.capacity_volume

    def get_occupied_volume(self):
        return self.occupied_volume



if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
