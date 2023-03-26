x = int(input())

First_number = x // 1000
Second_number = (x // 100) % 10
Third_number = (x // 10) % 10 
Forth_number = x % 10 

print(f"{Second_number}{First_number}{Forth_number}{Third_number}")