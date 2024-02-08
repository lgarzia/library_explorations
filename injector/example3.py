from typing import NewType

from injector import Binder, Module, inject, provider

Name = NewType("Name", str)
Description = NewType("Description", str)


class User:
    @inject
    def __init__(self, name: Name, description: Description):
        self.name = name
        self.description = description


# class UserModule(Module):
#    def configure(self, binder: Binder):
#        binder.bind(User)


class UserAttributeModule(Module):
    def configure(self, binder: Binder):
        binder.bind(Name, to="Sherlock")

    @provider
    def describe(self, name: Name) -> Description:
        return "%s is a man of astounding insight" % name


from injector import Injector

# injector = Injector([UserModule(), UserAttributeModule()])
injector = Injector([UserAttributeModule()])
injector.get(Name)
injector.get(Description)

user = injector.get(User)
user.nameuser.name
