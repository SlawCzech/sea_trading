class X:
    def __init__(self, value):
        self.value = value

    def _value_get(self):
        return self._value

    def _value_set(self, val):
        if not isinstance(val, int):
            raise TypeError('Something is no yes!')

        self._value = val

    def _value_del(self):
        print('***** ***')
        del self._value

    value = property(_value_get, _value_set, _value_del)


# x = X(42)
# print(x.value)
# x._value = 666
# print(x.value)
# x.value = 42
# print(x.value)
# del x.value

class A:
    # @staticmethod
    # def magic():
    #     print('magic a')
    pass


class B:
    # @staticmethod
    # def magic():
    #     print('magic b')
    pass


class C(B, A):
    pass


# c = C()
# c.magic()


class Z:
    def __init__(self, value):
        self.value = value

    def get_uppercase(self):
        return self.value.upper()


class Z1(Z):
    def __init__(self, value):
        super().__init__(value)

    def get_uppercase(self):
        return int(self.value) + 1


z = Z('ala')
print(z.get_uppercase())

z1 = Z1(42)
print(z1.get_uppercase())

print('Text ' + z1.get_uppercase())