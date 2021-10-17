class CoordinatesError(ValueError):
    pass


class CoordinatesTooLongError(CoordinatesError):
    pass


class CoordinatesTooShortError(CoordinatesError):
    pass


class NonIntegerCoordinatesError(CoordinatesError):
    pass


class CoordinatesTooSmallError(CoordinatesError):
    pass


class CoordinatesTooBigError(CoordinatesError):
    pass


class SpaceAlreadyOccupiedError(CoordinatesError):
    pass
