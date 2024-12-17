from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
       if not isinstance(capacity_volume, (int,float)):
           raise TypeError("ERRROR")
       if not capacity_volume>0:
           raise ValueError("ERRROR")
       self.occipied_volume=occupied_volume # TODO инициализировать объект "Стакан"
       if not isinstance(capacity_volume, (int,float)):
           raise TypeError("ERRROR")
       if not capacity_volume>0:
           raise ValueError("ERRROR")
       self.capacity_volume = capacity_volume



if __name__ == "__main__":
    Glass_1=Glass(20,40) # TODO инициализировать два объекта типа Glass
    Glass_2=Glass(20,15)
    Glass_3=Glass(-20,15)
    # TODO попробовать инициализировать не корректные объекты
help.glass
