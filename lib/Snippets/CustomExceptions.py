"""
This is an example of Custom Exception Class.
A custom exception class can be declared by inheriting the `Exception` Class.
Hierarchy can be achieved by inheriting in the right order.
"""


class Point(Exception):
    """ Raise some exception related to a point """
    def __init__(self, *args, **kwargs):
        # Add kwargs to dict store (if any)
        self.__dict__.update(kwargs)

        # Add this Class's message; In this case we're using the class's name
        args += (Point.__name__.lower(), )

        # Initialize super class; It does not accept kwargs
        super(Point, self).__init__(*args)

        self._set_message()

    def __str__(self):
        return '{}Exception: {}'.format(
            self.__class__.__name__, self.message)

    def _set_message(self):
        """ Set Error Message for this Exception """
        self.message = ' <= '.join(
            filter(
                lambda x: isinstance(x, str),
                self.args
            )
        )


class LineSegment(Point):
    """ This exception is part of Point Exception """
    def __init__(self, *args, **kwargs):
        # Add this class's message to the list
        args += (LineSegment.__name__.lower(), )
        super(LineSegment, self).__init__(*args, **kwargs)


class Square(LineSegment):
    def __init__(self, *args, **kwargs):
        args += (Square.__name__.lower(), )
        super(Square, self).__init__(*args, **kwargs)


class Cube(Square):
    def __init__(self, *args, **kwargs):
        args += (Cube.__name__.lower(), )
        super(Cube, self).__init__(*args, **kwargs)


class Tesseract(Cube):
    def __init__(self, *args, **kwargs):
        args += (Tesseract.__name__.lower(), )
        super(Tesseract, self).__init__(*args, **kwargs)


class CubeND(Exception):
    """
    N-Cube Exception Class that behaves according to param provided
    In this case `dimension` parameter is used to determine the
    behavior of this Exception
    """
    _CubeDimensions = (
        'point', 'linesegment', 'square', 'cube', 'tesseract', 'penteract',
        'hexeract', 'hepteract', 'octeract', 'enneract', 'dekeract'
    )

    def __init__(self, *args, **kwargs):
        # Add kwargs to dict store
        self.__dict__.update(kwargs)

        # Initialize the super class; It does not accept kwargs
        super(CubeND, self).__init__(*args)

        # Set message
        self._set_message()

    def __str__(self):
        return '{}Exception: {}'.format(
            CubeND._CubeDimensions[self.dimension].capitalize(),
            self.message
        )

    def _set_message(self):
        if hasattr(self, 'dimension'):
            # `dimension` variable is added to this instance when we update
            # its dict store with kwargs received in constructor
            self.dimension = self.dimension if self.dimension < 11 else 10
        else:
            self.dimension = 0  # Set default
        self.message = ' <= '.join(
            [CubeND._CubeDimensions[i] for i in range(self.dimension, -1, -1)]
        )


if __name__ == '__main__':

    # This is how Exception works by default
    try:
        raise Exception('Something bad happened')
    except Exception as e:
        print(e)

    # Multiple args for Exception returns a tuple
    try:
        raise Exception('Something bad happened', 'Code is broken')
    except Exception as e:
        print(e)

    # Hierarchical Exception
    try:
        raise Tesseract()  # Child level Exception
    except Point as e:  # This can be captured with the parent Exception
        print(e)

    # Parameterized Exception
    try:
        raise CubeND(dimension=10)  # Passing param `dimension`
    except CubeND as e:
        print(e)
