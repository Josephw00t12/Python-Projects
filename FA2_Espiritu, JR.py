print("FA2 Question 1")
def multList():
    answers = 1
    numbers = []
    while True:
        while True:
            try:
                x = int(input("Add a Number to the List: "))
                break
            except ValueError:
                print("\nNot a Valid Number! Please Input Again\n")
        numbers.append(x)
        print("\nValid Number\n")
        while True:
            try:
                a = int(input("Do you want to add again? 1.Yes 2.No: "))
                break
            except ValueError:
                print("\nNot a Valid Number! Please Input Again\n")
        if a == 2:
            break
        else:
            print("\nOkay!\n")

    for i in numbers:
        print(str(i) + " " , end=" ")
    for k in numbers:
        answers = answers * k
    return answers


print("\nThe Answer is: " + str(multList()))
print()

def sGrid():
    size = []
    while True:
        try:
            w = int(input("Width of the Grid: "))
            size.append(w)
            break
        except ValueError:
            print("\nNot a Valid Number! Please Input Again\n")
    while True:
        try:
            h = int(input("Height of the Grid: "))
            size.append(h)
            break
        except ValueError:
            print("\nNot a Valid Number! Please Input Again\n")
    return size



def rcGrid():
    rc = []
    while True:
        try:
            r = int(input("Rows of the Grid: "))
            rc.append(r)
            break
        except ValueError:
            print("\nNot a Valid Number! Please Input Again\n")
    while True:
        try:
            c = int(input("Columns of the Grid: "))
            rc.append(c)
            break
        except ValueError:
            print("\nNot a Valid Number! Please Input Again\n")
    return rc

def grid(rc,wh):
    rows = rc[0]
    columns = rc[1]
    width = wh[0]
    height = wh[1]
    #Top left Generation
        #Row Then Columns
    for r in range(rows):
        for c in range(columns):
            print("#",end="")
            for w in range(width):
                print(" ~ ", end="")
        # Ending Segment #
        for c in range(columns - (columns -1)):
            print("#",end="")
        # Going Down Segment    
        print()        
        for h in range(height):
            print("!", end="")
            # Middle segment and End segment ! printing
            for c in range(columns):
                for w in range(width):
                    print("   ", end="")
                print("!", end="")
            print()
    # Bottom Segment Ending        
    for c in range(columns):
        print("#",end="")
        for w in range(width):
            print(" ~ ", end="")
    print("#")

print("FA2 Question 2")

roco = rcGrid()
wihe = sGrid()
grid(roco, wihe)
