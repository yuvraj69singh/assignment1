print("============ QUESTION 1 ===========")
#QUESTION 1
a = int (input("Enter First Number: "))
b = int (input("Enter Second number: "))
c = int (input("Enter Third number: "))
avg = (a+b+c)/3
print("The average is :",avg)
print("============ QUESTION 2 ===========")
#QUESTION 2
income = int(input("Please enter your income: "))
dependents = int(input("Please enter number of dependents: "))
sd = 10000

taxable = income - sd - (dependents*3000)
tax = taxable*0.2
print("Total Payable tax is: ",tax)
print("============ QUESTION 3 ===========")

#QUESTION 3
student =[]
sid = int(input("Enter your SID: "))
name = str(input("Enter your name: "))
gender = str(input("Enter your Gender(M/F/U): "))
course_name = str(input("Enter your Course: "))
cgpa = float(input("Enter your cgpa: "))

student.append(sid)
student.append(name)
student.append(gender)
student.append(course_name)
student.append(cgpa)

print(student)
print("============ QUESTION 4 ===========")
#QUESTION 4
list = []
m1 = int(input("Marks of 1st student : "))

m2 = int(input("Marks of 2nd student : "))

m3 = int(input("Marks of 3rd student : "))

m4 = int(input("Marks of 4th student : "))

m5 = int(input("Marks of 5th student : "))

list.append(m1)
list.append(m2)
list.append(m3)
list.append(m4)
list.append(m5)

print("The list of marks of students is : ",list)

print("============ QUESTION 5 ===========")
#QUESTION 5
color = [ 'Red','Green','White','black','Pink','Yellow']
color.remove('black')
print("Updated list: ",color)
color[3] = ('purple')
print(color)
