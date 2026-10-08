list=[]
for i in range(3):
    name=input("enter your name:")
    age=int(input("enter your age:"))
    salary=int(input("enter your salary:"))
    tuple=(name,age,salary)
    list.append(tuple)
print(list)