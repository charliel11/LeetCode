class Solution:
    def __init__(self, name: str) -> None:
        import importlib

        module = importlib.import_module(f"leetcode.{name}")

        setattr(
            self.__class__, name, module.__getattribute__("Solution").__dict__[name]
        )
