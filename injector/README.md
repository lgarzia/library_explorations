# Notes

- [taskweaver](https://pypi.org/project/taskweaver/)
- [injector](https://pypi.org/project/injector/)
- https://injector.readthedocs.io/en/latest/api.html#injector.inject

- [dependency-injector](https://pypi.org/project/dependency-injector/)

While dependency injection is easy to do in Python due to its support for keyword arguments, the ease with which objects can be mocked and its dynamic nature, a framework for assisting in this process can remove a lot of boiler-plate from larger applications. That’s where Injector can help. It automatically and transitively provides dependencies for you. As an added benefit, Injector encourages nicely compartmentalised code through the use of modules.

[martinfowler](https://martinfowler.com/articles/injection.html)

I use **component** to mean a glob of software that's intended to be used, without change, by an application that is out of the control of the writers of the component. By 'without change' I mean that the using application doesn't change the source code of the components, although they may alter the component's behavior by extending it in ways allowed by the component writers.

A **service** is similar to a component in that it's used by foreign applications. The main difference is that I expect a component to be used locally (think jar file, assembly, dll, or a source import). A _service will be used remotely through some remote interface_, either synchronous or asynchronous (eg web service, messaging system, RPC, or socket.)

**injector**:
It comes into its own on large projects where the up-front effort pays for itself in two ways:

Forces decoupling. In our example, this is illustrated by decoupling our configuration and database configuration.

After a type is configured, it can be injected anywhere with no additional effort. Simply @inject and it appears. We don’t really illustrate that here, but you can imagine adding an arbitrary number of RequestHandler subclasses, all of which will automatically have a DB connection provided.

[terminology](https://injector.readthedocs.io/en/latest/terminology.html)

Injector is simply a dictionary for mapping types to things that create instances of those types. This could be as simple as:
`{str: 'an instance of a string'}`

### Abstractions:

- Provider:
  - ClassProvide - new instance
  - InstanceProvider - return existing instance
  - CallableProvider - calls a function
- Scope:
  - By default executed each time an instance is required
  - SingletonScope
  - threading-scoped
  - request-scoped
- Bind**ing**: ...?
  - A binding is the mapping of a unique binding key to a corresponding provider
- Bind**er**
  - The Binder is simply a convenient wrapper around the dictionary that maps types to providers. It provides methods that make declaring bindings easier.
- Module:
  - A Module configures bindings. It provides methods that simplify the process of binding a key to a provider.
  - `from injector import Module`
- Inject**ion**:
  - Injection is the process of providing an instance of a type, to a method that uses that instance. It is achieved with the inject decorator. Keyword arguments to inject define which arguments in its decorated method should be injected, and with what
- Inject**or**: The Injector brings everything together. It takes a list of Module s, and configures them with a binder, effectively creating a dependency graph:
- Assisted injection: Sometimes there are classes that have injectable and non-injectable parameters in their constructors.
- AssistedBuilder[T] and ClassAssistedBuilder[T] are injectable just as anything else, if you need instance of it you just ask for it like that:
- Child Injectors: This way you can have one injector that inherits bindings from other injector (parent) but these bindings can be overriden in it and it doesn’t affect parent injector bindings

per Bard:

#

By decoupling classes from their dependencies through dependency injection, you allow them to focus on their core responsibilities rather than worrying about creating or managing their dependencies. This leads to:

Reduced code duplication: Classes no longer need to implement common functionality like creating or configuring their dependencies, eliminating redundant code.
Improved modularity: Each class becomes a distinct, self-contained unit with clear responsibilities.
Loose coupling: Classes become less dependent on the implementation details of their dependencies, making them more adaptable and easier to change.

## Here's a breakdown of the boilerplate code that Injector can help remove in Python dependency injection:

### 1. Manual Object Creation and Configuration:

- **Without Injector:** You'd create instances of classes with their dependencies manually, often using `__init__()` constructors and passing arguments:

  ```python
  database = DatabaseConnection()
  user_service = UserService(database)
  ```

- **With Injector:** You define dependencies and let Injector handle instantiation and wiring:

  ```python
  injector = Injector()
  injector.bind(DatabaseConnection)
  injector.bind(UserService)
  user_service = injector.get(UserService)  # Injector creates and injects dependencies
  ```

### 2. Dependency Passing Throughout Layers:

- **Without Injector:** You'd pass dependencies explicitly through multiple function calls:

  ```python
  def create_user(user_data, database):
      user_service = UserService(database)
      user_service.create_user(user_data)

  create_user(data, database)
  ```

- **With Injector:** Dependencies are implicitly injected as needed:

  ```python
  @injector.inject
  def create_user(user_data, user_service: UserService):  # Injector provides UserService
      user_service.create_user(user_data)

  create_user(data)  # Injector passes UserService automatically
  ```

### 3. Mocking for Testing:

- **Without Injector:** You'd manually create mock objects and pass them during testing:

  ```python
  mock_database = MockDatabase()
  user_service = UserService(mock_database)
  ```

- **With Injector:** You can bind mock implementations for testing:

  ```python
  injector.clear_bindings()
  injector.bind(DatabaseConnection, MockDatabase)  # Bind mock for testing
  user_service = injector.get(UserService)  # Injector uses the mock
  ```

### 4. Managing Dependencies in Large Applications:

- **Without Injector:** Manually tracking and managing dependencies in complex applications can become cumbersome and error-prone.

- **With Injector:** Dependency relationships are defined centrally, reducing manual management and promoting consistency.

### 5. Dependency Resolution for Transitive Dependencies:\*\*

- **Without Injector:** You'd handle nested dependencies yourself, ensuring correct instantiation and configuration.

- **With Injector:** It automatically resolves transitive dependencies, ensuring all required objects are created and injected correctly.

By removing this boilerplate, Injector streamlines dependency injection, making code more concise, maintainable, and testable.
