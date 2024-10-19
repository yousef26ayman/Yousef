from datetime import date

date_of_birth = int(input("In which year you took birth:- "))

today_date = date.today().strftime("%Y")

print("your curret age is ",int(today_date)-date_of_birth)
