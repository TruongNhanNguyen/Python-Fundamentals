import unittest
from typing import Any, Callable, Tuple


def type_check(func: Callable) -> Callable:
    def wrapper(*args: Tuple[Any, ...], **kwargs: Any) -> Any:
        for i, (arg, arg_type) in enumerate(zip(args, func.__annotations__.values())):
            if not isinstance(arg, arg_type):
                raise TypeError(f"Argument {i+1} of {func.__name__} should be {arg_type}, not {type(arg)}")
        return func(*args, **kwargs)

    return wrapper


@type_check
def my_function(a: int, b: str) -> str:
    return f"{a} and {b}"


class TestTypeCheck(unittest.TestCase):
    def test_valid_arguments(self):
        result = my_function(1, "hello")
        self.assertEqual(result, "1 and hello")

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            my_function(1, 2)


if __name__ == '__main__':
    unittest.main()
