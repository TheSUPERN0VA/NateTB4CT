"""

Program Goals:
1: Get input from the user (at multiple points)
2: We need to convert some of this input to INTs from STRs
3: We need to provide choices to the user
    a. Add more values to a list
    b: Return a value at a specific index
"""
import random
myList = []
unique_list = []

def mainProgram():
    
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to a list or
2: Add a bunch of numbers
3. Return a value at an index
4. Sort List
5. Random Search
6. Recursive Binary Search
7. Linear Search
8. Recursive Binary Search
9. Iterative Binary Search
Print List
Quit  """)
        #add a way to catch bad user responses
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":    
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                searchItem = input("What are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
            elif choice == "7":
                searchItem = input("What are you looking for?  ")
                result = iterativeBinarySearch(unique_list, int(searchItem))
                if result != -1:
                    print("Your number is at index {}".format(result))
                else:
                    print("Your number isn't in that list!")
            elif choice == "8":
                sortList(myList)
                print("Your number is not found in that list, bud!")
            elif choice == "9":
                printLists()
            else:            
                break
        except:
            print("You made a whoopsie!")
        
    
def addToList():
    """
    This lets us add a single integer of our choice to the code
    """
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))

def addABunch():
    """
    This allows us to add several integers at once going up to a max value of our choice
    """
    print("We're gonna add a bunch of numbers to your list!")
    numToAdd = input("How many new integers would you like to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")    
    
def indexValues():
    """
    This function will print the number at any index position on our list
    """
    print("At what index position do you want to search")
    indexPos = input("Type n index position here:   ")
    print(myList[int(indexPos)])

def sortList(myList):
    """
    With this we can sort the integers in the default list the program gives us and make a new one
    """
    print("A little bird told me you needed some data.")
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list? Y/N  ")
    if showMe.lower() == "y":
        print(unique_list)

def randomSearch():
    """
    This function will give us a random number from the list
    """
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])
    if len(unique_list) > 0:
           print(unique_list[random.randint(0, len(unique_list)-1)])
    
def linearSearch():
    """
    This will ma e the program go through each index postition one at a time and give us every index position where a number we want is at
    """
    print("We're gonna check out each item one at a time in your list. This sucks!")
    searchValue = input("What you looking for?  ")
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    """
    This will print the number we want over and over every time it's on the list
    """
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("You ding dang found it at index position {}".format(mid))
            return mid
        elif unique_list[mid] >= x:
            return recuriveBinarySearch(unique_list, low, mid -1, x)

        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mide + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    """
    This function will look for the number you want, showing every number along the way utnil it find what you want
    """
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid - 1
        else:
                return mid
    return -1

def printLists():
    """
    Self explanatory. It prints your list out entirely
    """
    if len(unique_list) == 0:
        print(myList)
    else:
            whichOne = input("Which list? Sorted or unsorted?  ")
            if whichOne.lower() == "sorted":
                print(unique_list)
            else:
                    print(myList)
    
if __name__ == "__main__":
    mainProgram()
