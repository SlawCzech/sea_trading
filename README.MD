# Sea trading

## Python OOP
- class 
- object 
- self
- method 
  - default (self)
  - staticmethod ()
  - classmethod(cls)
- field/attribute
  - object field (self)
  - class field
- python features (magic methods)
  - `__str__` -> string
  - `__len__` -> int
  - `__repr__` -> string
  - `__format__` -> string
  - `__name__` -> string
  - `__init__` -> None
  - `__new__` -> self/object
- constructor - metoda tworząca obiekt (__new__)
- object descriptor/data object descriptor (getters/setters/deleter)
  - property - class data object descriptor protocol
- super - 
- MRO - method resolution order (C3)


## OOP Rules
1. Abstraction
2. Inheritance
3. Polymorphism - różne zachowania w zależności od kontekstu wywołania
4. Encapsulation

## SOLID
1. Single responsibility principle
2. Open/Closed principle
3. Liskov substitution principle
4. Interface segregation principle
5. Dependency inversion principle

## Hierarchy
- Interface - zbiór zasad, które muszą być zaimplementowane, żeby to coś było czymś, np. auto musi mieć koła, jeździć itp. Nie zawiera żadnego szczegółu implementacyjnego! Nie ma tego w Pythonie!
- Abstract Class - też requirements, partially implementation details
- Concrete Class - implementation details

## Hierarchy 2
- metaclass - służą do tworzenia klas (ale to też klasa)
- class - służą do tworzenia obiektów
- object - instancja klasy


## Examples
```python

class X:
  b = 'on class'
  
  def __init__(self):
    self.a = 'on instance'
    print(self.a)
    print(X.b)
    self.a = 're-bound'
    self.b = 'new one instance'
    print(self.b)
    print(X.b)
    

```