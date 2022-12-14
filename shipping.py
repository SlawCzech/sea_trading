import iso6346


class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.length_ft = length_ft
        self.owner_code = owner_code
        self.contents = contents
        self.bic = type(self)._make_bic_code(owner_code=owner_code, serial=ShippingContainer._generate_serial())
        # self.serial = ShippingContainer._generate_serial()

    @property
    def volume_ft3(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents)

        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, new_celsius):
        if new_celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError('Too hot')
        self._celsius = new_celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6), category='R')

    @property
    def volume_ft3(self):
        return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, value):
        if not (HeatedRefrigeratedShippingContainer.MIN_CELSIUS <= value <= RefrigeratedShippingContainer.MAX_CELSIUS):
            raise ValueError('Temperature out of range.')
        # self._celsius = value
        RefrigeratedShippingContainer.celsius.fset(self, value)

sc = ShippingContainer('ELO', 200, ['drugs'])
rsc = RefrigeratedShippingContainer('ELO', 200, ['drugs'], celsius=3.0)
hrsc = HeatedRefrigeratedShippingContainer('ELO', 200, ['drugs'], celsius=3.0)
rsc2 = RefrigeratedShippingContainer.create_empty('ELO', 200, celsius=3.0)
# print(rsc.bic)
# print(ShippingContainer.next_serial)
# print(sc.next_serial)
print(sc.volume_ft3)
print(rsc.volume_ft3)
hrsc.celsius = -21
print(hrsc.celsius)
