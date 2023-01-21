import typing as ty

A = ty.TypeVar("A")
B = ty.TypeVar("B")
IterA = ty.Iterable[A]
IterB = ty.Iterable[B]
A_B = ty.Callable[[A], B]
A_IterB = ty.Callable[[A], IterB]
IterA_IterB = ty.Callable[[IterA], IterB]
IterA_B = ty.Callable[[IterA], B]


class Functor(ty.Generic[A]):
    def __init__(self, value: A):
        self.value: A = value

    def apply(self, func: A_B) -> "Functor[B]":
        return Functor(func(self.value))

    def split(self, func: A_IterB) -> "IterFunctor[B]":
        return IterFunctor(func(self.value))


class IterFunctor(ty.Generic[A]):
    def __init__(self, value: IterA):
        self.value: IterA = value

    def apply(self, func: IterA_IterB) -> "IterFunctor[B]":
        return IterFunctor(func(self.value))

    def map(self, func: A_B) -> "IterFunctor[B]":
        return IterFunctor(map(func, self.value))

    def flat(self, func: IterA_B) -> Functor[B]:
        return Functor(func(self.value))
