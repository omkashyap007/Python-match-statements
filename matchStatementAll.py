from dataclasses import dataclass


a = "Nothing else and this is not the case"
a = "Something important"
print(a.split()) 

match a.split() : 
    case ["Nothing" ] : 
        print("This the first one !")

    case ["Nothing" , *c] : 
        print("This is the second one  !")

    case "Someone" :  
        print("This is third one !")

    case "Something else": 
       print("This is the fourth  one !") 
       
    case other  :
        print("This is the final case !")


# using a pipe operator for or clause in the  match statement . 

print("-----------------------------------------")
print("We cannot use or in the match case and we have to use pipe oprator in place of or !")
a = "Someone" 

match a :
#    case "Om" or "Someone" : 
#        print("The very first of the second for the or case")
    case "Om"| "Someone" | "Something else" : 
        print("The name is om or something")

    case "Om"  : 
        print("The name is only om ")

    case "Someone":
        print("The name is someone")


# using offgaurd in python

print("---------------------------------------------")


check_list  = ["Hello" , "World" , "Someone" ]  
a = "Someone Hello"
match a.split() : 
    case "Someone"  if a in check_list : 
        print("It is in the check list and it is printed !")

    case "Om" : 
        print("The name of the parameter is  Om")

    case other : 
        print("This is the other case !")


print("-----------------------------------------------------")
# using composable  ( the pattern is composable ) i can put a pattern in the other pattern to  match . 
a =  "Someone Known"
match a.split() : 
    case ["Someone" ,("Unknown" | "Known") as person]  :
        print(f"There is a car and it  is {person}")

    case other : 
        print("The person is not known !")

print("------------------------------------------------------")
# using structural pattern matching for classes and  its instances .


@dataclass
class Employee:
    name : str
    pay  :  float
    language : str


@dataclass
class Programmer  :
    name : str
    backend : str
    frontend : str
    speed :  int

emp1 = Employee("Om" , 50000.00  , "Python")
emp2 = Employee("Someone"  ,   20000.00 ,  "C++")


programmer1 = Programmer("Om" , "Django" , "React" , "101")
programmer2 = Programmer("Someone" , "Laravel"  , "Vue" , "80")

match programmer1 : 
    case Employee(x , y , "Python"):
        print("This is a python programmer Employee")

    case Programmer("Om" , a , c , "101") :
        print("He is a python programmer with speed of 101  wpm")

    case Employee(a , b , c):
        print("He is just an employee")

    case _ : 
        print("I don't know")

# using dictionary matching .

d =  {"name" : "Om" , "language" : "Python" , "framework":   "Django" }

match  d : 
    case {"name" :  "Om" } : 
        print("The  other values  are  not taken  in context , if the key name is present and its value is Om , this will  run")
        print("The name of the person  is   Om")
    case _ :
        print("Hello")


