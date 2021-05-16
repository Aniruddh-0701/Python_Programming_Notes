class Student:
    obj_count = 0
    stud_list = dict()

    def __init__(self, rn=0, st_name="Name", *clubs):  # Parametric Constructor
        Student.obj_count += 1
        self.roll_no = rn
        self.name = st_name
        self.club = list(clubs)
        Student.stud_list[rn] = st_name
        # {roll_no: st_name}

    def study(self):
        print(f"{self.name} is Studying....")

    def wake(self):
        self.study()
        return "Woke"

    def __del__(self):  # destructor
        Student.obj_count -= 1
        Student.stud_list.pop(self.roll_no)

    def __repr__(self):  # String representation
        return f"Roll no.: {self.roll_no} \nName: {self.name}\n" f"Clubs: {self.club}"

    def __lt__(self, obj):  # Less than
        return self.name < obj.name

    def __le__(self, obj):  # Less than or equal
        return self.name <= obj.name

    def __gt__(self, obj):  # Greater than
        return self.name > obj.name

    def __ge__(self, obj):  # Greater than or equal
        return self.name >= obj.name

    def __ne__(self, obj):  # Not equal
        return self.name != obj.name

    def __eq__(self, obj):  # Equal
        return self.name == obj.name

    def __getitem__(self, key):
        return self.club[key - 1]

    def __setitem__(self, key, value):
        self.club[key - 1] = value

    def __len__(self):
        return len(self.club)
    
    # getter
    @property
    def roll_no(self):
        # print('Getter called')
        return self.__roll_no

    # setter
    @roll_no.setter
    def roll_no(self, rn):
        # print('Setter called')
        self.__roll_no = rn


# Object 1
st1 = Student(1, "Prabhu", "Coding Club", "Robotics Club")
print(st1)
st1[2] = 'Envy Club'
print(st1)
