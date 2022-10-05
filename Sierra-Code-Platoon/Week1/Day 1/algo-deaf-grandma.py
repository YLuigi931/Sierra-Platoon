def deaf_grandma():
    
    counter = 1
    ans = input("HEY KID!")
    
    while(counter != 3):
        ask = input("WHAT!")
        if(ask.isupper() and ask != "GOODBYE!"):
            print("NO, NOT SINCE 1946!")
        elif(ask.isupper() == False and len(ask)>0):
            print("SPEAK UP, KID!")
            if(ask == "GOODBYE!" and counter < 2):
                print("LEAVING SO SOON?")
                counter += 1
        elif(ask == "GOODBYE!" and counter < 2):
            print("LEAVING SO SOON?")
            counter += 1
        elif(ask == "GOODBYE!" and counter == 2):
            print("LATER, SKATER!")
            counter += 1
            

deaf_grandma()