# TODO Добавить методы add_water и remove_water
class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int, add_water: None, remove_water:None):
        self.capacity_volume = capacity_volume
        #get_capacity_volume()
        self.occupied_volume = occupied_volume
        #get_occupied_volume()
        self.add_water = None
        get_add_water()
        self.remove_water = None
        get_remove_water()

    def get_capacity_volume(self):
        return self.capacity_volume

    def get_occupied_volume(self):
        return self.occupied_volume

    def get_add_water(self):
        TypeError

        if self.add_water + self.occupied_volume > self.capacity_volume:
            ValueError
            else self.occupied_volume+=self.add_water

        if self.add_water > self.capacity_volume:
            ValueError
            else self.occupied_volume+=self.add_water

        return self.add_water

    def get_remove_water(self):
        TypeError
        if self.occupied_volume - self.remove_water < 0:
            ValueError
            else self.occupied_volume -= self.add_water


        return self.remove_water
