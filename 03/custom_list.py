from typing import List


class CustomList(list):
    def __repr__(self):
        return f"Elems: {super().__repr__()}\nSum: {sum(self)}"

    def __add__(self, other: List):
        result = []
        copy_self = self.copy()
        copy_other = other.copy()
        while len(copy_self) > len(copy_other):
            copy_other.append(0)
        while len(copy_self) < len(copy_other):
            copy_self.append(0)
        for i, j in zip(copy_self, copy_other):
            result.append(i + j)
        return CustomList(result)

    def __radd__(self, other: List):
        result = []
        copy_self = self.copy()
        copy_other = other.copy()
        while len(copy_self) > len(copy_other):
            copy_other.append(0)
        while len(copy_self) < len(copy_other):
            copy_self.append(0)
        for i, j in zip(copy_self, copy_other):
            result.append(i + j)
        return CustomList(result)

    def __sub__(self, other):
        result = []
        copy_self = self.copy()
        copy_other = other.copy()
        while len(copy_self) > len(copy_other):
            copy_other.append(0)
        while len(copy_self) < len(copy_other):
            copy_self.append(0)
        for i, j in zip(copy_self, copy_other):
            result.append(i - j)
        return CustomList(result)

    def __rsub__(self, other):
        result = []
        copy_self = self.copy()
        copy_other = other.copy()
        while len(copy_self) > len(copy_other):
            copy_other.append(0)
        while len(copy_self) < len(copy_other):
            copy_self.append(0)
        for i, j in zip(copy_self, copy_other):
            result.append(j - i)
        return CustomList(result)

    def __eq__(self, other):
        # Из условия: (сравнение с list не нужно)
        if not isinstance(other, CustomList):
            return False
        return sum(self) == sum(other)

    def __ne__(self, other):
        # Из условия: (сравнение с list не нужно)
        if not isinstance(other, CustomList):
            return False
        return sum(self) != sum(other)

    def __le__(self, other):
        # Из условия: (сравнение с list не нужно)
        if not isinstance(other, CustomList):
            return False
        return sum(self) <= sum(other)

    def __lt__(self, other):
        # Из условия: (сравнение с list не нужно)
        if not isinstance(other, CustomList):
            return False
        return sum(self) < sum(other)

    def __ge__(self, other):
        # Из условия: (сравнение с list не нужно)
        if not isinstance(other, CustomList):
            return False
        return sum(self) >= sum(other)

    def __gt__(self, other):
        # Из условия: (сравнение с list не нужно)
        if not isinstance(other, CustomList):
            return False
        return sum(self) > sum(other)
