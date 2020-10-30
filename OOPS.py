class Student:
    obj_count = 0
    stud_list = dict()
    
    def __init__(self, rn =0, st_name = 'Name'): # Parametric Constructor
        Student.obj_count += 1
        self.roll_no = rn
        self.name = st_name
        stud_list[rn] = st_name
    
    def study(self):
        print(f'{self.name} is Studying....')

    def __del__(self): # destructor
        Student.obj_count -= 1

    @property
    def roll_no(self):
        print('Getter called')
        return f'Roll no: {self._roll_no}'

    @roll_no.setter
    def roll_no(self, rn):
        print('Setter called')
        self._roll_no = rn
        
    
    
    
# Object 1
st1 = Student(1, 'Prabhu')
print(st1.roll_no)
print(st1.name)

print()

#Object 2

st2 = Student(2, 'Ani')
print(st2.roll_no)
print(st2.name)
print()
print(Student.obj_count)
print()

del st2
print(Student.obj_count)

