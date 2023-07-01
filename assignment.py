people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for person, gender, person_age in zip(people,sex,age):
   interpolated_string = f"{person} the {gender} is {person_age} years old."
   print(interpolated_string)
