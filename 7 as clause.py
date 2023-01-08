def runMatch(string):
    data = string.split()
    match data :
        case ["walk" , ("east"  | "north" | "west" |  "south" ) as direction ] : 
            print(f"We are going to walk to the {direction}")
        
        case ["drive"  , ("uphill" | "downhill") as slope ] : 
            print(f"We are going to drive to the {slope}")
            
        case _  :  
            print("We are going nowhere !")
            
if __name__ == "__main__"  : 
    runMatch(("walk  east"))
    runMatch(("walk  south"))
    runMatch(("walk  north"))
    runMatch(("drive uphill"))
    runMatch(("drive downhill"))