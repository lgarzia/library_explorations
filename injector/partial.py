from injector import Injector, get_bindings, inject, noninjectable


@inject
class A:
    @noninjectable("b")
    def __init__(self, a: int, b: str) -> None:
        self.a = a
        self.b = b


print(get_bindings(A.__init__))

from injector import ClassAssistedBuilder


def configure(binder):
    binder.bind(int, to=123)


injector = Injector(configure)
builder = injector.get(ClassAssistedBuilder[A])
b = "this is b"  # define B
obj = builder.build(b=b)
print(obj.a, obj.b)
