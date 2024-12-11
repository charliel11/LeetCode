from pathlib import Path

import pytest

from leetcode import Solution
from loader import dynamical_loader, generate_loader_type_hint

targets = [name.stem for name in Path("test/data/").glob("*")]


@pytest.mark.parametrize("Target", targets)
def test_target(Target):
    TestCasePath = f"test/data/{Target}"
    f = Solution(Target).__getattribute__(Target)

    print()
    for *args, answer in dynamical_loader(
        Path(TestCasePath), generate_loader_type_hint(f)
    ):
        print(args, answer)
        assert f(*args) == answer
