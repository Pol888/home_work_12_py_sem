import random


class Rectangle:
    __slots__ = ('_length', '_width')
    def __init__(self, length, width=None):
        self._length = length
        self._width = width
        if width is None:
            self._width = length

    @property
    def length_and_width(self):
        return f"{self._length = } and {self._width = }"

    @length_and_width.setter
    def length_and_width(self, length_and_width):
        if type(length_and_width) == int:
            if length_and_width < 0:
                raise ValueError
            else:
                self._length = length_and_width
        elif len(length_and_width) == 2:
            if length_and_width[0] < 0 or length_and_width[1] < 0:
                raise ValueError
            else:
                self._length = length_and_width[0]
                self._width = length_and_width[1]
        else:
            raise ValueError

    def rectangle_perimeter(self):
        return 2 * self._length + 2 * self._width

    def area_of_a_rectangle(self):
        return self._width * self._length

    def __add__(self, other):
        p = (self.rectangle_perimeter() + other.rectangle_perimeter()) / 2
        side_one = random.randint(1, p)
        site_two = p - side_one
        return Rectangle(int(side_one), int(site_two))

    def __sub__(self, other):
        if self.rectangle_perimeter() - other.rectangle_perimeter() > 0:
            p = (self.rectangle_perimeter() - other.rectangle_perimeter()) / 2
        elif self.rectangle_perimeter() - other.rectangle_perimeter():
            return None
        else:
            p = (other.rectangle_perimeter() - self.rectangle_perimeter()) / 2
        side_one = random.randint(1, p)
        site_two = p - side_one
        return Rectangle(int(side_one), int(site_two))

    def __eq__(self, o) -> bool:
        return self.rectangle_perimeter() == o.rectangle_perimeter()

    def __ne__(self, o) -> bool:
        return self.rectangle_perimeter() != o.rectangle_perimeter()

    def __gt__(self, o) -> bool:
        return self.rectangle_perimeter() > o.rectangle_perimeter()

    def __ge__(self, o) -> bool:
        return self.rectangle_perimeter() <= o.rectangle_perimeter()

    def __lt__(self, o) -> bool:
        return self.rectangle_perimeter() < o.rectangle_perimeter()

    def __le__(self, o) -> bool:
        return self.rectangle_perimeter() >= o.rectangle_perimeter()


if __name__ == '__main__':
    p_1 = Rectangle(8, 4)
    p_1.length_and_width = 3, 7
    print(p_1.length_and_width)
    print(p_1.__slots__)
