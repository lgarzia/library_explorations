from injector import Injector, inject


class Inner:
    def __init__(self):
        self.forty_two = 42


class Outer:
    @inject
    def __init__(self, inner: Inner):
        self.inner = inner


injector = Injector()
outer = injector.get(Outer)
print(outer.inner.forty_two)

# #
# inner = Inner()
# outer = Outer(inner)  # alternative
# outer.inner.forty_two
# outer.inner.forty_two
