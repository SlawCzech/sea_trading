import iso6346


class ShippingContainer:
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
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = type(self)._make_bic_code(owner_code=owner_code, serial=ShippingContainer._generate_serial())
        # self.serial = ShippingContainer._generate_serial()


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents)

        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, new_celsius):
        if new_celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError('Too hot')
        self._celsius = new_celsius


    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6), category='R')


sc = ShippingContainer('ELO', ['drugs'])
rsc = RefrigeratedShippingContainer('ELO', ['drugs'], celsius=3.0)

print(rsc.bic)
# print(ShippingContainer.next_serial)
# print(sc.next_serial)
