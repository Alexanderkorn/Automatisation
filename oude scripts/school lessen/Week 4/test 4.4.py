__author__ = 'alexander'

#Python 3.3.3

import sys #Allows use of the 'exit()' function
import csv #Allows use of the CSV File API

def mainMenu():
    print("########################################################")
    print("# Welcome to the recipe book, please select an option: #")
    print("# 1. Add new recipe                                    #")
    print("# 2. Lookup existing recipe                            #")
    print("# 3. Exit                                              #")
    print("########################################################")

    selectedOption = None
    inputtedOption = input()

    try:
        inputtedOption = int(inputtedOption)
    except ValueError:
        print("Invalid option entered")

    if inputtedOption == 1:
        selectedOption = inputtedOption
    elif inputtedOption == 2:
        selectedOption = inputtedOption
    elif inputtedOption == 3:
        print("Exiting...")
        sys.exit(0)

    return selectedOption

def validateInput(inputtedData):
    try: #Test if data is an integer greater than 1
        inputtedData = int(inputtedData)
        if int(inputtedData) < 1: #Recipes cannot contain less than 1 ingredient
            print("Sorry, invalid data entered.\n('%s' is not valid for this value - positive integers only)" % inputtedData)
            return False
        return int(inputtedData)
    except ValueError:
        print("Sorry, invalid data entered.\n('%s' is not valid for this value - whole integers only [ValueError])\n" % inputtedData)
        return False

def addRecipe():
    print("Welcome to recipe creator! The following questions will guide you through the recipe creation process.\nPlease enter the name of your recipe (e.g. 'Pizza'):")
    recipeName = input()
    print("Recipe Name: %s" % recipeName)
    print("Please enter the amount of people this recipe serves (e.g. '6'):")
    recipeServingAmount = input()
    if validateInput(recipeServingAmount) == False:
        return
    else:
        recipeServingAmount = validateInput(recipeServingAmount)
    print("Recipe serves: %s" % recipeServingAmount)
    print("Please enter the number of ingredients in this recipe (e.g. '10'):")
    recipeNumberOfIngredients = input()
    if validateInput(recipeNumberOfIngredients) == False:
        return
    else:
        recipeNumberOfIngredients = validateInput(recipeNumberOfIngredients)
    print("Recipe contains: %s different ingredients" % recipeNumberOfIngredients)
    ingredientList = {}
    i = 1
    while i <= recipeNumberOfIngredients:
        nthFormat = "st"
        if i == 2:
            nthFormat = "nd"
        elif i == 3:
            nthFormat = "rd"
        elif i >= 4:
            nthFormat = "th"
        ingredientNumber = str(i) + nthFormat
        print("Please enter the name of the %s ingredient:" % ingredientNumber)
        ingredientName = input()
        print("Please enter the quantity of the %s ingredient:" % ingredientNumber)
        ingredientQuantity = input()
        print("Please enter the measurement value for the %s ingredient (leave blank for no measurement - e.g. eggs):"  % ingredientNumber)
        ingredientMeasurement = input()
        print("%s ingredient: %s%s %s" % (ingredientNumber, ingredientQuantity, ingredientMeasurement, ingredientName))
        finalIngredient = [ingredientName, ingredientQuantity, ingredientMeasurement]
        print(finalIngredient[1])
        ingredientList[i] = finalIngredient
        with open('recipes/' + recipeName + '.csv', 'w') as csvfile:
            recipewriter = csv.writer(csvfile)
            recipewriter.write(ingredientList[0])
            recipewriter.write(ingredientList[1])
            recipewriter.write(ingredientList[2])

        i = i + 1

def lookupRecipe():
    pass  # To-do: add CSV reader and string formatter

#Main flow of program
while True:
    option = mainMenu()

    if option == 1:
        addRecipe()
    elif option == 2:
        lookupRecipe()