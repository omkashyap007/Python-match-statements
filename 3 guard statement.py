# using if statement in python , which  are called guard statements . 

def provideAccess(user) : 
    return {
        "username" : user , 
        "password" : "admin"
    }

    
def runMatch()  : 
    user = str(input("Write your username -: "))
    allowedDataBaseUsers  = ["Rishabh"]
    match user :  
        case "Rishabh" if user in allowedDataBaseUsers :
            print("You are allowed to access the database !")
            data =  provideAccess("Rishabh")
            print(data)
        case _ : 
            print("You are not a company memeber , you are not  allowed to access the code !")

if __name__ == "__main__" :  
    for _ in range(2) : 
        runMatch()
            