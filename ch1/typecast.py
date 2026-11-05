"""Type casting demo"""

num1 = int("32")                #string to int
num2 = float("3.14")            #string to float
str_num = str(100)              #int to string
truncated_num = int(3.99)       #float to int (truncates decimal part)

# result1 = "Coding" + 7        #TypeError: can only concatenate str (not "int") to str
result2 = "Coding" + str(7)     #Correct way to concatenate string to int
result3 = 5 + 3.2               #int + float results in float

#Μετατροπές bool
#Ψευδή θεωρούνται τα εξής: 0, 0.0, "", []. {}, None

bool1 = bool(0)
bool2 = bool(1)
bool3 = bool("Hello")
bool4 = bool("")

print("Num1 is:" + str(num1))
print("Num2 is:" + str(num2))