import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any, Callable, Type, TypeVar, get_args, get_type_hints

T = TypeVar("T", bound=tuple[Any, ...])
U = TypeVar("U")


def parse(txt: str, t: Type[U]) -> U:
    res = json.loads(txt)
    return res


def dynamical_loader(file: Path, t: Type[T]) -> Iterator[T]:
    txt = file.read_text().split("\n")
    hints = get_args(t)
    assert len(txt) % len(hints) == 0

    for i in range(0, len(txt), len(hints)):
        res = ()
        for j, hint in enumerate(hints):
            res += (parse(txt[i + j], hint),)
        yield res


def generate_loader_type_hint(f: Callable) -> Type[T]:
    type_hints = get_type_hints(f)
    return tuple[tuple([v for _k, v in type_hints.items()])]
