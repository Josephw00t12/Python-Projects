#FA3 Q1
print("Question 1")
def printEven(num):
    for e in num:
        if (e % 2) != 1:
            print(e)


numbers = [1,2,3,4,5,6,7,8,9,10,11,13,15,17,19,24,26,28,30,32]
printEven(numbers)

print("\n")
print("Question 2")
#FA3 Q2
def genEven():
    genList = []
    for i in range(10,61):
        if i%2 !=1:
            genList.append(i)
    printEven(genList)

genEven()

print("\n")
print("Question 3")
#FA3 Q3
def get_feu_professor():
    ps = []
    for i in range(5):
        name = input("Number " + str(i+1) + " Professor's Name: ")
        ps.append(name)
        while True:
            try:
                ans = int(input("Do you know the Salary? 1.Yes 2.No: "))
                if ans > 2 or ans < 1:
                    print("Invalid Input")
                    continue
                break
            except ValueError:
                print("Invalid Input")
        if ans == 1:
            while True:
                try:
                    sal = int(input(ps[i+i]+ "'s " + " Salary:  "))
                    break
                except ValueError:
                    print("Invalid Input")
        else:
            print("Then it will be assumed 70000php")
            sal = 70000
        print()
        sal = str(sal)
        ps.append(sal)
    return ps

def show_feu_professor(prsa):
    for i in range(0,10,2):
        print(prsa[i] + " with a Salary of " + prsa[i+1] + "php")
        print()

profsal = get_feu_professor()
print()
show_feu_professor(profsal)
