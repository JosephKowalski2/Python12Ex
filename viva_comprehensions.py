from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start: integer number to start
    :param stop: integer number to stop
    :param parity: determines whether odd or even values are returned
    :return: list of odd or even numbers in start stop range
    """
    return [value for value in range(start, stop) if
            (parity == parity.EVEN and value % 2 == 0) or (parity == parity.ODD and value % 2 != 0)]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start: integer value to start at
    :param stop: integer value to end before
    :param strategy: math function used on value
    :return: dictonary key of integer number and value of key value after math function used
    """
    return {number: strategy(number) for number in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    pass
