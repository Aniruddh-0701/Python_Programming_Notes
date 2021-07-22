from __future__ import annotations

from typing import Any, Literal, Union


class Student(object):
    student_count: int = 0
    stud_list: dict[int, str] = dict()
    __roll_no: int = 0
    name: str
    club: list[Any]

    def __new__(cls, rn: int = 0, st_name: str = "Name", *clubs: Any) -> Student:
        print("__new__ magic method is called to create an obj\n")
        inst: Student = super().__new__(cls)
        return inst

    # Parametric Constructor
    def __init__(self, rn: int = 0, st_name: str = "Name", *clubs: Any) -> None:
        Student.student_count += 1
        self._roll_no = rn
        self.name = st_name
        self.club = list(clubs)
        Student.stud_list[rn] = st_name
        # {_roll_no: st_name}

    def study(self) -> None:
        print(f"{self.name} is Studying....")

    @staticmethod
    def wake() -> str:
        # self.study()
        return "Woke"

    # destructor
    def __del__(self) -> None:
        Student.student_count -= 1
        Student.stud_list.pop(self._roll_no)

    # String representation of Object
    def __repr__(self) -> str:
        return f"Roll no.: {self._roll_no} \nName: {self.name}\n" f"Clubs: {self.club}"

    # Less than
    def __lt__(self, obj: Student) -> bool:
        return self.name < obj.name

    # Less than or equal
    def __le__(self, obj: Student) -> bool:
        return self.name <= obj.name

    # Greater than
    def __gt__(self, obj: Student) -> bool:
        return self.name > obj.name

    # Greater than or equal
    def __ge__(self, obj: Student) -> bool:
        return self.name >= obj.name

    # Not equal
    def __ne__(self, obj: Student) -> bool:
        return self.name != obj.name

    # Equal
    def __eq__(self, obj: Student) -> bool:
        return self.name == obj.name

    def __getitem__(self, key: int) -> str:
        return self.club[key - 1]

    def __setitem__(self, key: int, value: Union[str, Literal]) -> None:
        self.club[key - 1] = value

    def __len__(self) -> int:
        return len(self.club)

    # getter
    @property
    def _roll_no(self) -> int:
        # print('Getter called')
        return self.__roll_no

    # setter
    @_roll_no.setter
    def _roll_no(self, rn: int) -> None:
        # print('Setter called')
        if self._roll_no in Student.stud_list.keys():
            Student.stud_list.pop(self.__roll_no)
            Student.stud_list[rn] = self.name
        self.__roll_no = rn


# Object 1
st1 = Student(1, "Prabhu", "Coding Club", "Robotics Club")
print(st1)

print(Student.student_count)
print(Student.stud_list, "\n")

st1[2] = "Envy Club"
print(st1)

st2 = Student(3, "Mano", "Coding Club", "Cyber club")
print("\n", st2, "\n", sep="")
print(Student.student_count)
print(Student.stud_list, "\n")

st2._roll_no = 2

print("\n", Student.student_count, sep="")
print(Student.stud_list, "\n")

del st2

print("\n", Student.student_count)
print(Student.stud_list, "\n")
