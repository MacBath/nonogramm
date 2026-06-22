import sys
from pathlib import Path


class NumberGroup:
    def __init__(self, groups: list[int]):
        self.__groups = groups

    @property
    def Elements(self) -> int:
        return len(self.__groups)

    @property
    def TotalSum(self) -> int:
        return sum(self.__groups) + self.Elements - 1

    def __repr__(self) -> str:
        return f"[{', '.join(str(item) for item in self.__groups)}]"

    def __str__(self) -> str:
        return self.__repr__()


class Block:
    def __init__(self, x0: int, x1: int):
        self.x0 = x0
        self.x1 = x1


class Nonogramm:
    def __init__(
        self,
        widht: int,
        height: int,
        h_groups: list[NumberGroup],
        v_groups: list[NumberGroup],
    ):
        self.width = widht
        self.height = height
        self.groups_horizontal = h_groups
        self.groups_vertical = v_groups

    def validate_config(self) -> bool:
        """Validate Config

        Returns:
            Validation Success
        """
        if self.width > 0 and len(self.groups_horizontal) != self.width:
            return False
        elif self.height > 0 and len(self.groups_vertical) != self.height:
            return False

        for group in self.groups_horizontal:
            if group.TotalSum > self.height:
                return False
        for group in self.groups_vertical:
            if group.TotalSum > self.width:
                return False
        return True

    @classmethod
    def load_from_file(
        cls, file_name: Path, encoding: str = "UTF-8", sep: str = " "
    ) -> "Nonogramm":
        with open(file_name, "r", encoding=encoding) as nono_file:
            t_width, t_height = nono_file.readline().split(sep)
            width = int(t_width)
            height = int(t_height)
            h_groups: list[NumberGroup] = []
            v_groups: list[NumberGroup] = []

            for _ in range(width):
                t_group: list[int] = []
                for element in nono_file.readline().split(sep):
                    t_group.append(int(element))
                h_groups.append(NumberGroup(t_group))
            for _ in range(height):
                t_group: list[int] = []
                for element in nono_file.readline().split(sep):
                    t_group.append(int(element))
                v_groups.append(NumberGroup(t_group))
            nonogramm = Nonogramm(width, height, h_groups, v_groups)
            if nonogramm.validate_config():
                return nonogramm

            raise ValueError("File does not contain valid Nonogramm data")


def main():
    nonogramm = Nonogramm.load_from_file(Path(sys.argv[1]).resolve())
    pass


if __name__ == "__main__":
    main()
