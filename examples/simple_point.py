from pysketcher import Parameter, ConstrainedObject, Scalar


class Point(ConstrainedObject):
    x = Parameter(Scalar)
    y = Parameter(Scalar)


p = Point("p")
q = Point("q")

q.x = p.x + p.y
p.x = 3.

print(repr(p.x))
print(repr(q.x))
print(p.parameters)
print(q.parameters)
