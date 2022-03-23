from pysketcher import ConstrainedValue, ConstrainedObject, Scalar

class Point(ConstrainedObject):
    x = ConstrainedValue(Scalar)
    y = ConstrainedValue(Scalar)

p = Point("p")
q = Point("q")

q.x = p.x
p.x = 3.

print(repr(p.x))
print(repr(q.x))
print(p.parameters)
print(q.parameters)