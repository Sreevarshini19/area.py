a=int(input("Enter your mark:"))
if a>=90:
    grade='O'
elif a>=80:
    grade='A+'
elif a>=70:
    grade='A'
elif a>=60:
    grade='B'
elif a>=50:
    grade='C'
else:
    grade="Fail"
print("Your grade is",grade)