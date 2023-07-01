str = "The quick brown fox jumps over the lazy dog"
print(str)
print(len(str))
print(str.upper())
print(str.lower())
print(str.title())

str_rev = "The quick brown fox jumps over the lazy dog" [::-1]
print(str_rev)
print(str.title())
print(str.count("a"))
print(str.count("the"))
print(str.replace("the", "a"))

freq = {}
for i in str:
        if i in freq:
               freq[i] += 1
        else:
             freq[i] = 1
	 
print(freq)


people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for person, gender, person_age in zip(people,sex,age):
   interpolated_string = f"{person} the {gender} is {person_age} years old."
   print(interpolated_string)
