class Bottle:

    def __init__(self, capacity_l):
        if not type(capacity_l) in (int, float):
            raise TypeError(f"Capacity must be a number")
        if capacity_l <= 0:
            raise ValueError("Value must be highr than 0")
        self.capacity_l = capacity_l
        self.volume_l = 0
        self.closed = False


    def set_volume_l(self, value):
        #if not isinstance(value, (int, float)):
        if not type(value) in (int, float):
            raise TypeError(f"Volume must be a number")
        elif not self.closed:
            raise Exception(f"The lid is closed")
        elif value < 0:
            raise ValueError("Volume must be bigger or equal 0")
        else:
            self.volume_l = value

    def set_volume_ml(self, value):
        if not type(value) in (int, float):
            raise TypeError(f"Volume must be a number")
        elif not self.closed:
            raise Exception(f"The lid is closed")
        elif value < 0:
            raise ValueError("Volume must be bigger or equal 0")
        else:
            self.volume_l = value

    def close(self):
        self.closed = True

    def open(self):
        self.closed = False

    def empty(self):
        self.volume_l = 0

    def get_volume_ml(self) -> float:
        return self.volume_l * 1000.0

    def get_volume_l(self):
        return self.volume_l

    def set_volume_ml(self, value_ml: float):
        if not type(value_ml) in (int, float):
            raise TypeError(f"Volume must be a number")
        elif not self.closed:
            raise Exception(f"The lid is closed")
        elif value_ml < 0:
            raise ValueError("Volume must be bigger or equal 0")
        else:
            self.volume_l = value_ml / 1000.0