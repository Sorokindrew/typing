"""
TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""

import typing
T = typing.TypeVar('T')


class Foo:
    def return_self(self: T) -> T:
        ...