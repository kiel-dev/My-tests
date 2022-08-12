#Age to years, months and day to days converter
#Developer: Ezequiel 

month_tab = (31,28,31,30,31,30,31,31,30,31,30,31)
out = 0

print("Testing algorithm in python\n")

year =  input("How old are you in years? ")
month = input("How old are you in months?")
day = input("How old are you in days?")

for p in range(int(year)):
	out = out + 365

for p in range(int(month)):
	out = out + month_tab[p]

result = out + int(day)

print("Your age in days is:" , result)

