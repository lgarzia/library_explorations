from simple import Inner, Outer

from injector import Binder, Injector, Module, provider


# Bind new Innter Module
class InnerModule(Module):
    @provider
    def create_test_user(self) -> Inner:
        inner = Inner()
        inner.forty_two = 55
        return inner


def test_outer_forty_two():
    injector = Injector([InnerModule()])
    outer = injector.get(Outer)
    assert outer.inner.forty_two == 55


class InnerModule2(Module):
    def configure(self, binder: Binder) -> None:
        inner = Inner()
        inner.forty_two = 55
        binder.bind(Inner, to=inner)


def test_outer_forty_two_b():
    injector = Injector([InnerModule2()])
    outer = injector.get(Outer)
    assert outer.inner.forty_two == 55


def test_outer_forty_two_lw():
    inner = Inner()
    inner.forty_two = 55
    outer = Outer(inner)
    assert outer.inner.forty_two == 55


# def test_outer_forty_two_wb():
#     inner = Inner()
#     inner.forty_two = 55
#     injector = Injector()
#     injector.binder.bind(Inner, to=inner)
#     outer = injector.create_object(Outer)
#     assert outer.inner.forty_two == 55


def test_outer_forty_two_wb2():
    inner = Inner()
    inner.forty_two = 55
    injector = Injector()
    injector.binder.bind(Inner, to=inner)
    outer = injector.get(Outer)
    assert outer.inner.forty_two == 55
    assert outer.inner.forty_two == 55
