class Shoe:
    def __init__(self, brand, style, size, color):
        self.brand = brand
        self.style = style
        self.size = size
        self.color = color
        self.condition = "Old"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)) or value < 1:
            raise ValueError("Size must be a positive number")
        self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"