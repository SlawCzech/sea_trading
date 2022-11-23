# TODO pobawię się klasą (dodać podróże, jak to działa i w ogóle)

class Itinerary:

    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)

    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return "\n".join(location.name for location in self._locations)

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]

    @property
    def destination(self):
        return self._locations[-1]

    def add(self, location):
        self._locations.append(location)

    def remove(self, name):
        self._locations = [location for location in self._locations if location.name != name]

    def truncate_at(self, name):
        stop = None

        for idx, location in enumerate(self._locations):
            if location.name == name:
                stop = idx + 1
                break

        self._locations = self._locations[:stop]