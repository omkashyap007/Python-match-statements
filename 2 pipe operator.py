# using or clause in python statements using pipe operator . 

def provideAccess(user) : 
    return {
        "username" : user , 
        "password" : "admin"
    }

    
def runMatch()  : 
    user = str(input("Write your username -: "))
    match user :  
        case "Om" |  "Vishal"  : 
            print("You are not allowed to access the database !")
        
        case "Rishabh" :
            print("You are allowed to access the database !")
            data =  provideAccess("Rishabh")
            print(data)
        case _ : 
            print("You are not a company memeber , you are not  allowed to access the code !")

if __name__ == "__main__" :  
    for _ in range(2) : 
        runMatch()
            