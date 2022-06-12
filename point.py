

class Point():

  def __init__(self, x, y):
      self.x = x
      self.y = y


# вычисление расстояния до центра координат
  def dist_to_0(self):
      return (self.x ** 2 + self.y ** 2) ** (1/2)


# сложение координат двух точек 
  def __add__(self, other):
      return Point(self.x + other.x, self.y + other.y)


# вычисление расстояния между двумя точками
  def dist_between_points(self, other):
      return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

p1 = Point(1, 1)
p2 = Point(-1, -1)

p1.dist_to_0() # вывод результата первого метода

p3 = p1 + p2
print('Point3',  p3) # вывод результата второго метода

print(p1.dist_between_points(p2)) # вывод результата третьего метода


