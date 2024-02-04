
# Menu available in the coffee machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# resources to make coffee available in machine

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# how much money collected in machine

moneyOnMachine = 0

# this decided if the machine should stop on secret command of "off"

machineStatus = "ON"


# TODO 2: Check function to check the availability of material for the new order
def check(demand):
    if demand=='report':    #report is a valid secret input and so in order to prevent error (error as there is no report thing in menu), we must deal with it
        return
    elif demand == "latte" or demand == "espresso" or demand == "cappuccino":  # this checks if sufficient resources/material is avaiable in machine to make the coffee
        for _ in MENU[demand]["ingredients"]:
            if MENU[demand]["ingredients"][_] > resources[_]:
                print(f"Sorry! There is not enough {_}")
                return
    else:                               # deals with invalid input given by user which is not available in machine
        print("Invalid request !!")
        return
    menucost=MENU[demand]["cost"]
    print(f"\nYour Coffee will be ready soon !! \n\nKindly pay $ {menucost} before :")
    moneyProcess(demand)

# this function helps taking coins from the user, this prevents any non integer input and asks the user to enter again
def takeintinput(cointype, demand):
    amount = 0
    try:
        amount = int(input(f"{cointype} : "))
    except ValueError:
        print("Invalid input. Please enter an integer")
        takeintinput(cointype, demand)
    return amount


# TODO 3: moneyProcess function to take money from the user and calculate if sufficient money is provided
def moneyProcess(demand):
    quarters = takeintinput("quarters", demand)
    dimes = takeintinput("dimes", demand)
    nickel = takeintinput("nickel", demand)
    pennies = takeintinput("pennies", demand)

    totalMoneyReceived = quarters * 0.25 + nickel * 0.05 + pennies * 0.01 + dimes * 0.10
    if totalMoneyReceived < MENU[demand]["cost"]:
        print(f"Total amount paid : $ {totalMoneyReceived}")
        print("Sorry that's not enough money \nNo Money charged !!")
        return
    else:
        print(f"Total amount paid : $ {totalMoneyReceived}")
        transaction(totalMoneyReceived, demand)


# TODO 4: transaction finalise the cost, return the excess amount and update the resources avaibale in machine
def transaction(totalMoney, demand):

    for _ in resources:
        resources[_] -= MENU[demand]["ingredients"][_]
    global moneyOnMachine
    moneyOnMachine = MENU[demand]["cost"]

    moneytoreturn=totalMoney-MENU[demand]["cost"]
    moneytoreturn=round(moneytoreturn,3)
    print(f"Here is $ {moneytoreturn} in change. \nThanks for the payment !")
    print(f"\nHere is your amazing {demand} !! \n")

def reportprint(demand):
    print("\nResources we have :")
    for _ in resources:
        print(f"{_} : {resources[_]}")
    print(f"Money : $ {moneyOnMachine}\n")




# TODO 1: runMachine function is the main function that runs, turns off the machine, and calls the required variable to initiate the order
def runMachine():
    while machineStatus == 'ON':
        print("Order from our premium coffee machine!!")
        demand = input("What would you like? (espresso/latte/cappuccino) ")
        if demand == 'off':
            print("Turning Off!")
            return

        if demand == 'report':
            reportprint(demand)

        check(demand)


# this function will start the machine
runMachine()
