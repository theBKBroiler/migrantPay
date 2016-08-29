import sys

def workerName():

    running = True

    totalFlats = 0
    while running:

        #ask for worker name
        print('Please enter worker name: ')
        name = input()
        print("Worker: " + name)
        print()

        #ask how many flats they picked
        print('How many flats did ' + name + ' pick?')
        flats = input()
        flats = int(flats)
        totalFlats += flats

        #multiply by 3 as they get $3/flat
        print(name + ' will be paid $' + str(flats * 3) + ' today')
        print()

        #get hourly wage (total pay divided by hours picked)
        print('How many hours was ' + name + ' picking?')
        hours = input()
        hours = float(hours)
        print()
        wage = ((flats * 3) / hours)
        #round to hudredths place bc money
        print(name + ' got paid $' + str(round(wage, 2)) + '/hr')
        print()

        print('Would you like to process another worker?')
        print('Type 1 for yes and 0 for no')
        choice = input()
        if choice == '0':
            running = False
            jPay = float(input('How much to pay Jorge?\n$'))
            print('Total number of flats: ' + str(totalFlats))
            totalPay = ((totalFlats * 3) + jPay)
            #print('Total amount paid out: $' + (str(totalFlats * 3)) + (str(jPay)))
            print('Total amount paid out: $' + str(totalPay))
            print('Thanks for running this program!')
        elif choice == '1':
            continue
        else:
            print("Please type 1 or 0")

workerName()
