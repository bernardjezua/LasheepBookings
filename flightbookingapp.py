"""
Flight Booking Application

"""
from datetime import *  # for deptime, depdate, esttime
from tabulate import tabulate # for viewing of seats

flight = {}  # flight dictionary
passengers = {}  # passengers


def flightID(flight):  # function for flightID increment
    count = len(flight) + 1
    if count > 0 and count <= 9:
        flight_id = "000" + str(
            count
        )  # updates if count is greater than 0 and less than 10
    elif count >= 10 and count < 100:
        flight_id = "00" + str(count)  # updates if count is 10 to 99
    else:
        flight_id = "0" + str(count)  # updates if count is greater than 99
    return flight_id


def getDate(string, digits): # function for getting date
    while True:
        num = input(string)
        if len(num) == digits:
            try:
                num = int(num)
                return num
            except:
                print("Input must be an Integer!\n")
        else:
            print("Invalid! Follow the format or input must be an Integer!\n")


def getTime(string): # function for getting time
    while True:
        time = input(string)
        # Check Format if Valid
        if (len(time)) == 5: # limits length of time input to 5
            if time[2] == ":": # checks if : is at the 3rd part of the string
                try:
                    num1 = int(time[0:1]) 
                    num2 = int(time[3:4])
                    return time
                except:
                    print("Invalid Input. Follow Format!\n")
            else:
                print("Invalid Input. Follow Format!\n")
        else:
            print("Invalid Input. Follow Format!\n")


def checkAircraftAvailability(flight, name, depdate, deptime, esttimearr): # checks aircraft availability
    # Checks if aircraft already exist
    isPresent = False
    flightkey = []
    if flight != 0:
        for fkey in flight.keys():
            if flight[fkey]["Aircraft"] == name:
                isPresent = True
                flightkey.append(fkey)
    if isPresent == True:
        for i in flightkey:
            # Checks if same Departure Date
            if str(flight[i]["DepDate"]) == str(depdate):
                # Checks if in Conflict with time

                # The new departure time must be within the boundaries of the already scheduled flight to return False
                depsplit1 = flight[i]["DepTime"].split(":")
                depsplit2 = deptime.split(":")

                estsplit = flight[i]["EstTimeArr"].split(":")
                if depsplit2[0] >= depsplit1[0] and depsplit2[0] <= estsplit[0]:
                    return False
    return True


def addFlight(flight):  # function for adding flights
    global passengers
    print("\n. . . . . ╰──╮ DEPARTURE AND DESTINATION ╭──╯ . . . . .")
    name = input("Enter Aircraft Name: ")  # asks user for input

    while True:
        deploc = input("Enter Departure Location: ")
        desloc = input("Enter Destination Location: ")
        if deploc != desloc:
            break
        else:
            print("\nDeparture and Destination Location must not be the same!\n Enter another.\n")

    while True:
        print("\n. . . . . ╰──╮ DATE AND TIME ╭──╯ . . . . .")
        print("\n>> Departure Date <<\n")

        depdate = None
        estdatearr = None

        # Checks if date is valid
        while True:
            try:
                dep_month = getDate("Month (MM): ", 2)
                dep_date = getDate("Date (DD): ", 2)
                dep_year = getDate("Date (YYYY): ", 4)

                depdate = date(dep_year, dep_month, dep_date)
                break
            except:
                print("Invalid Date!\n")

        deptime = getTime("Departure Time (24H - HH:MM): ") # input must be 24h format
        splitdept = deptime.split(":")

        print("\n. . . . . ╰──╮ ESTIMATED ARRIVAL ╭──╯ . . . . .")

        print("\n>> Estimated Date <<\n")

        while True:
            try:
                est_month = getDate("Month (MM): ", 2)
                est_date = getDate("Date (DD): ", 2)
                est_year = getDate("Date (YYYY): ", 4)
                estdatearr = date(est_year, est_month, est_date)
                break
            except:
                print("Invalid Date!\n")

        esttimearr = getTime("Estimated Time of Arrival (24H - HH:MM): ")
        splitest = esttimearr.split(":")

        # Checks if date and time is Logical
        if estdatearr >= depdate:
            if splitest[0] == splitdept[0]:
                if splitest[1] > splitdept[1]:
                    break
                else:
                    print("\n>>> Estimated Time must be after the Departure Time!<<<\n")
            elif splitest[0] > splitdept[0]:
                break
            else:
                print("\n>>> Estimated Time must be after the Departure Time! <<<\n")
        else:
            print("\n>>> Estimated Date must be after the Departure Date! <<<\n")

    isAvailable = checkAircraftAvailability(flight, name, depdate, deptime, esttimearr)

    # prints out if aircraft is already available
    if isAvailable != True:
        print("\n>>> Conflict in Schedule for Aircraft", name, "<<<")
        print("Cancel Scheduling...\n")
        return

    flight_id = flightID(flight)

    print("\n. . . . . ╰──╮ MAX NO. OF PASSENGERS ╭──╯ . . . . .")
    while 1:
        maxPass = input("Enter the maximum number of passengers (10 or 15): ")
        if maxPass == "15":
            print(maxPass + " is the maximum number for Flight " + flight_id + ".")
            passengers[flight_id] = { # gives a dictionary of 15 passengers
                "A1": "A1", "B1": "B1", "C1": "C1",
                "A2": "A2", "B2": "B2", "C2": "C2",
                "A3": "A3", "B3": "B3", "C3": "C3",
                "A4": "A4", "B4": "B4", "C4": "C4",
                "A5": "A5", "B5": "B5", "C5": "C5",
            }
            break

        elif maxPass == "10":
            print(maxPass + " is the maximum number for Flight " + flight_id + ".")
            passengers[flight_id] = { # gives a dictionary of 10 passengers
                "A1": "A1", "B1": "B1",
                "A2": "A2", "B2": "B2",
                "A3": "A3", "B3": "B3",
                "A4": "A4", "B4": "B4",
                "A5": "A5", "B5": "B5",
            }
            break

        else:
            print(">>> Invalid entry. Please enter only a 10 or 15. <<<") # prints if input is not 10 or 15
            continue

    flight[flight_id] = {  # dictionary for flights
        "Aircraft": name,
        "DepLoc": deploc,
        "DesLoc": desloc,
        "DepDate": depdate,
        "DepTime": deptime,
        "EstDateArr": estdatearr,
        "EstTimeArr": esttimearr,
        "MaxPass": maxPass,
    }

    saveFlight(flight) # saves flight
    savePassengers(passengers) # saves passengers

    return flight, passengers


def editFlight(flight):  # definition for editing flight
    global passengers
    if len(flight) == 0:
        print(">>> No flights to edit! Create one first. <<<")
    else:
        while (1):
            print("\n. . . . . ╰──╮ EDITING FLIGHT ╭──╯ . . . . .")
            print("\n*⋆. Here are the Available Flight IDs: *⋆.")
            for i in flight.keys():  # prints each flight IDs available
                print(">>> " + i)
            choice = input("\nEnter Flight ID: ")

            if choice in flight.keys():  # edits the entire flight info
                print("\n. . . . . ╰──╮ DEPARTURE AND DESTINATION ╭──╯ . . . . .")
                name = input("Enter Aircraft Name: ")  # asks user for input

                while True:
                    deploc = input("Enter Departure Location: ")
                    desloc = input("Enter Destination Location: ")
                    if deploc != desloc:
                        break
                    else:
                        print("\nDeparture and Destination Location must not be the same!\n Enter another.\n")

                while True:
                    print("\n. . . . . ╰──╮ DATE AND TIME ╭──╯ . . . . .")
                    print("\n>> Departure Date <<\n")

                    depdate = None
                    estdatearr = None

                    # Checks if date is valid
                    while True:
                        try:
                            dep_month = getDate("Month (MM): ", 2)
                            dep_date = getDate("Date (DD): ", 2)
                            dep_year = getDate("Date (YYYY): ", 4)

                            depdate = date(dep_year, dep_month, dep_date)
                            break
                        except:
                            print("Invalid Date!\n")

                    deptime = getTime("Departure Time (24H - HH:MM): ") # input must be 24h format
                    splitdept = deptime.split(":")

                    print("\n. . . . . ╰──╮ ESTIMATED ARRIVAL ╭──╯ . . . . .")

                    print("\n>> Estimated Date <<\n")

                    while True:
                        try:
                            est_month = getDate("Month (MM): ", 2)
                            est_date = getDate("Date (DD): ", 2)
                            est_year = getDate("Date (YYYY): ", 4)
                            estdatearr = date(est_year, est_month, est_date)
                            break
                        except:
                            print("Invalid Date!\n")

                    esttimearr = getTime("Estimated Time of Arrival (24H - HH:MM): ")
                    splitest = esttimearr.split(":")

                    # Checks if date and time is Logical
                    if estdatearr >= depdate:
                        if splitest[0] == splitdept[0]:
                            if splitest[1] > splitdept[1]:
                                break
                            else:
                                print("\n>>> Estimated Time must be after the Departure Time!<<<\n")
                        elif splitest[0] > splitdept[0]:
                            break
                        else:
                            print("\n>>> Estimated Time must be after the Departure Time! <<<\n")
                    else:
                        print("\n>>> Estimated Date must be after the Departure Date! <<<\n")

                # updates value in dictionary, with maxPass as exception
            flight[choice]["Aircraft"] = name
            flight[choice]["DepLoc"] = deploc
            flight[choice]["DesLoc"] = desloc
            flight[choice]["DepDate"] = depdate
            flight[choice]["DepTime"] = deptime
            flight[choice]["EstDateArr"] = estdatearr
            flight[choice]["EstTimeArr"] = esttimearr
            print(">>> Flight successfully edited! <<<\n")
            break

        else:  # prints if input is not among available flight IDs
            print(">>> Something went wrong. Please try again! <<<")
    return flight


def delFlight(flight):
    if len(flight) == 0:  # checks if dictionary has key-value pair
        print(">>> No flights to delete! Create one first. <<<")
    else:
        while 1:
            print("\n*⋆. Here are the Available Flight IDs: *⋆.")
            for i in flight.keys():  # prints each flight IDs availa1ble
                print(">>> " + i)

            choice = input("\nEnter Flight ID: ")  # asks user for input
            if choice in flight.keys():  # deletes info of flight ID specified
                del flight[choice]
                print(">>> Flight " + choice + " successfully deleted! <<<")
                break
            else:
                print(">>> Something went wrong. Please try again! <<<")


def depTimeView(flight):  # function for departure time view
    print("\n. . . . . ╰──╮ DEPARTURE TIME ╭──╯ . . . . .")
    deptimesort = []
    for i in flight.keys():
        date = str(flight[i]["DepDate"]) + " " + str(flight[i]["DepTime"])
        deptimesort.append(date)
        
    deptimesort = sorted([datetime.strptime(dt, "%Y-%m-%d %H:%M") for dt in deptimesort]) # sorts list

    for i in deptimesort:
        sortingWithID = str(i) # gets string of elements in the list deptime sort
        comparethis = sortingWithID[0:16] # slices string to date and time
        for j in flight.keys():
            date2 = str(flight[j]["DepDate"]) + " " + str(flight[j]["DepTime"])
            if comparethis == date2: # if element in deptimesort is same as depdate and dep time, it prints out with flightID
                print(">>> Flight " + str(j) + " >>> " + str(comparethis))


def depLocView(flight): # function for departure location
    print("\n. . . . . ╰──╮ DEPARTURE LOCATION ╭──╯ . . . . .")
    for i in flight.keys():
        print("Flight " + str(i), ">>> " + str(flight[i]["DepLoc"]))


def nameView(flight):
    print("\n. . . . . ╰──╮ AIRCRAFT NAME ╭──╯ . . . . .")
    for i in flight.keys():
        print(">>> Flight " + str(i), ">>> Name: " + str(flight[i]["Aircraft"]))

def depdesLoc(flight):
    if len(flight) == 0:
        print(">>> No flights to view! Create one first. <<<")
    else:
        print("\n. . . . . ╰──╮ DEPARTURE AND DESTINATION ╭──╯ . . . . .")
        for i in flight.keys():
            print(
                "Flight " + str(i),
                ">>> " + str(flight[i]["DepLoc"]) + " >>> " + str(flight[i]["DesLoc"]))

def viewFlight(flight):
    if len(flight) == 0:  # checks if dictionary has key-value pair
        print(">>> No flights to view! Create one first. <<<")
    else:
        while 1:
            print(
                "What would you like to view?\n"
                "[1] - View By Departure Time\n[2] - View By Departure Location\n[3] - View By Aircraft Name\n"
                "[0] - Return to Main Menu\n")
            choice = input("Enter Choice: ")
            if choice == "1":
                depTimeView(flight) 
                break
            elif choice == "2":
                depLocView(flight)
                break
            elif choice == "3":
                nameView(flight)
                break
            elif choice == "0":
                break
            else:
                print(">>> Something went wrong. Please try again! <<<")
                continue

def viewFlight2(flight):
    if len(flight) == 0:  # checks if dictionary has key-value pair
        print(">>> No flights to view! Create one first. <<<")
    else:
        while 1:
            print("\n. . . . . ╰──╮ VIEWING OF SEATS ╭──╯ . . . . .")
            print(
                "What would you like to view?\n"
                "[1] - View By Departure Time\n[2] - View By Departure Location\n[3] - View By Departure and Destination\n"
                "[0] - Return to Main Menu\n")
            choice = input("Enter Choice: ")
            if choice == "1":
                depTimeView(flight)
                break
            elif choice == "2":
                depLocView(flight)
                break
            elif choice == "3":
                depdesLoc(flight)
                break
            elif choice == "0":
                break
            else:
                print(">>> Something went wrong. Please try again! <<<")
                continue

def searchAircraft(flight): # searching aircraft name
    print("\n. . . . . ╰──╮ SEARCHING AIRCRAFT ╭──╯ . . . . .")
    print("Note: The first letter of the aircraft or the whole name will both show flights.")
    while (1):
        choice = input("\nEnter Aircraft Name: ")
        choice.capitalize()
        for i in flight.keys():
            temp = flight[i]["Aircraft"]
            firstletter = temp[0]
            if choice in flight[i]["Aircraft"] or choice[0] == firstletter: # condition / ex. N will show Nreb, A will show AirAsia
                print(">>> Flight " + str(i) + " >>> " + str(flight[i]["Aircraft"]))
        break

def checkWeekday(dt2): # checks departure weekday
    if dt2 == "0":
        dt2 = "Monday"
    elif dt2 == "1":
        dt2 = "Tuesday"
    elif dt2 == "2":
        dt2 = "Wednesday"
    elif dt2 == "3":
        dt2 = "Thursday"
    elif dt2 == "4":
        dt2 = "Friday"
    elif dt2 == "5":
        dt2 = "Saturday"
    elif dt2 == "6":
        dt2 = "Sunday"
    return dt2

def checkWeekday2(dt4): # checks est weekday arrival
    if dt4 == "0":
        dt4 = "Monday"
    elif dt4 == "1":
        dt4 = "Tuesday"
    elif dt4 == "2":
        dt4 = "Wednesday"
    elif dt4 == "3":
        dt4 = "Thursday"
    elif dt4 == "4":
        dt4 = "Friday"
    elif dt4 == "5":
        dt4 = "Saturday"
    elif dt4 == "6":
        dt4 = "Sunday"
    return dt4

def searchDay(flight): 
    print("\n. . . . . ╰──╮ SEARCH VIA DAY ╭──╯ . . . . .")
    print("Note: You must input the whole word. Ex: Tuesday")
    choice3 = input("Enter day of the week: ")
    choice3 = choice3.capitalize()

    for i in flight.keys():
        dt = str(flight[i]["DepDate"])
        dt2 = str(datetime.strptime(dt, '%Y-%m-%d').weekday())

        dt3 = str(flight[i]["EstDateArr"])
        dt4 = str(datetime.strptime(dt3, '%Y-%m-%d').weekday())

        dt2 = checkWeekday(dt2)
        dt4 = checkWeekday2(dt4)

        if choice3 == dt2 or choice3 == dt4:
            print(">>> Flight " + str(i) + " >>> DEP DAY: " + str(dt2) + " >>> ARR DAY: " + str(dt4))

        

def searchFlight(flight):
    if len(flight) == 0:  # checks if dictionary has key-value pair
        print(">>> No flights to search! Create one first. <<<")
    else:
        while 1:
            print(
                "What would you like to search?\n"
                "[1] - Search Available Seats\n[2] - Search Aircraft\n[3] - Search Via Day\n"
            )
            choice = input("Enter Choice: ")
            if choice == "1":
                tabulateSeats(flight, passengers)
                break
            elif choice == '2':
                searchAircraft(flight)
                break
            elif choice == '3':
                searchDay(flight)
                break
            else:
                print(">>> Something went wrong. Please try again! <<<")
                continue


def adminControl(flight, passengers):
    loadFlight(flight)  # loads previous file with flight records
    loadPassenger(passengers) # loads file with passenger records
    print("\n.*. ⋆. *. Welcome aboard, Captain! *. ⋆. *. ⋆")
    while 1:
        print(
            "\nWhat would you like to do?\n"
            "[1] - Add a Flight\n[2] - Edit a Flight\n[3] - Delete a Flight\n[4] - View Flights\n[5] - Search Flights\n"
            "[0] - Return to Main Menu\n"
        )
        choice = input("Enter Choice: ")
        if choice == "1":
            addFlight(flight)
        elif choice == "2":
            editFlight(flight)
        elif choice == "3":
            delFlight(flight)
        elif choice == "4":
            viewFlight(flight)
        elif choice == '5':
            searchFlight(flight)
        elif choice == "0":
            break
        else:
            print(">>> Something went wrong. Please try again! <<<")


def checkAvailable(key): # increments if key of values are greater than 2
    counter = 0
    for i in passengers[key]:
        if len(passengers[key][i]) > 2:
            counter += 1
    return counter


def addPassenger(passengers): # allows passenger to book flight
    if len(flight) != 0:
        choice = tabulateSeats(flight, passengers) # gets choice through seat function
        if choice in flight.keys():
            if checkAvailable(choice) < int(flight[choice]["MaxPass"]):
                choice2 = input("\nEnter Seat Number: ")
                if (
                    choice2 in passengers[choice].keys()
                    and len(passengers[choice][choice2]) == 2
                ):
                    passengers[choice][choice2] = input(
                        "Enter Passenger Name (First Name): "
                    )
                    print(str(passengers[choice][choice2]), "has booked seat number", str(choice))
                    savePassengers(passengers)
                    return
                else:
                    print(">>> Seat is Already Taken / Does not Exist! <<<")
        else:
            print(">>> Flight does not exist! <<<")

    else:
        print("No Available Flights!\n")

def tabulateSeats(flight, passengers): # tabulates seats to 2x5 or 3x5
    while (1):
        print("\n. . . . . ╰──╮ VIEWING OF SEATS ╭──╯ . . . . .")
        print("*⋆. Here are the Available Flight IDs: *⋆.")
        for i in flight.keys():  # prints each flight IDs available
            print(">>> " + str(i))
        
        choice2 = input("\nEnter Flight ID: ")  # asks user for input
        if choice2 in flight.keys():  # deletes info of flight ID specified
            fileHandle = open("passengers.txt", "r")  # reads text file
            for line in fileHandle:
                flightline = line[:-1].split("<#>")  # splits each item followed by <#>
                if choice2 == flightline[0] and flight[flightline[0]]["MaxPass"] == "10":
                    print(tabulate([[flightline[1], flightline[2]], [flightline[3], flightline[4]], [flightline[5], flightline[6]],
                    [flightline[7], flightline[8]], [flightline[9], flightline[10]]]))
                elif choice2 == flightline[0] and flight[flightline[0]]["MaxPass"] == "15":
                    print(tabulate([[flightline[1], flightline[2], flightline[3]], [flightline[4], flightline[5], flightline[6]], [flightline[7], 
                    flightline[8], flightline[9]], [flightline[10], flightline[11], flightline[12]], [flightline[13], flightline[14], flightline[15]]]))
            fileHandle.close()
            break
        else:
            print(">>> Something went wrong. Please try again! <<<")
    return choice2

def passengerControl(passengers): # main control for passenger
    while True:
        print("\n>>> Passenger's Section <<<")
        choice = input("[1] - View Flights\n[2] - View Seats\n[3] - Book Flight\n[0] - Return to Main Menu\nEnter Choice: ")
        if choice == "1":
            viewFlight2(flight)
        elif choice == "2":
            tabulateSeats(flight, passengers)
        elif choice == "3":
            addPassenger(passengers)
        elif choice == "0":
            break
        else:
            print("Wrong Input! Please try again.\n")


def saveFlight(flight): # saves to txt file
    fileHandle = open("flights.txt", "w+")  # appends new line to flights.txt file
    for i in flight.keys():
        if i in flight.keys():
            fileHandle.write(
                str(i)
                + "<#>"
                + flight[i]["Aircraft"]
                + "<#>"
                + flight[i]["DepLoc"]
                + "<#>"
                + flight[i]["DesLoc"]
                + "<#>"
                + str(flight[i]["DepDate"])
                + "<#>"
                + flight[i]["DepTime"]
                + "<#>"
                + str(flight[i]["EstDateArr"])
                + "<#>"
                + flight[i]["EstTimeArr"]
                + "<#>"
                + flight[i]["MaxPass"]
                + "\n"
            )
    fileHandle.close()


def savePassengers(passengers): # saves passengers to txt file
    fileHandle = open("passengers.txt", "w+")
    for i in passengers.keys():
        if flight[i]["MaxPass"] == "10":
            fileHandle.write(
                str(i)
                + "<#>"
                + passengers[i]["A1"]
                + "<#>"
                + passengers[i]["B1"]
                + "<#>"
                + passengers[i]["A2"]
                + "<#>"
                + passengers[i]["B2"]
                + "<#>"
                + passengers[i]["A3"]
                + "<#>"
                + passengers[i]["B3"]
                + "<#>"
                + passengers[i]["A4"]
                + "<#>"
                + passengers[i]["B4"]
                + "<#>"
                + passengers[i]["A5"]
                + "<#>"
                + passengers[i]["B5"]
                + "\n"
            )
        else:
            fileHandle.write(
                str(i)
                + "<#>"
                + passengers[i]["A1"]
                + "<#>"
                + passengers[i]["B1"]
                + "<#>"
                + passengers[i]["C1"]
                + "<#>"
                + passengers[i]["A2"]
                + "<#>"
                + passengers[i]["B2"]
                + "<#>"
                + passengers[i]["C2"]
                + "<#>"
                + passengers[i]["A3"]
                + "<#>"
                + passengers[i]["B3"]
                + "<#>"
                + passengers[i]["C3"]
                + "<#>"
                + passengers[i]["A4"]
                + "<#>"
                + passengers[i]["B4"]
                + "<#>"
                + passengers[i]["C4"]
                + "<#>"
                + passengers[i]["A5"]
                + "<#>"
                + passengers[i]["B5"]
                + "<#>"
                + passengers[i]["C5"]
                + "\n"
            )
    fileHandle.close()


def loadPassenger(passengers): # loads passengers from txt file
    fileHandle = open("passengers.txt", "r+")  # reads text file
    for line in fileHandle:
        flightline = line[:-1].split("<#>")  # splits each item followed by <#>
        if flight[flightline[0]]["MaxPass"] == "10":
            passengers[flightline[0]] = {
                "A1": flightline[1],
                "B1": flightline[2],
                "A2": flightline[3],
                "B2": flightline[4],
                "A3": flightline[5],
                "B3": flightline[6],
                "A4": flightline[7],
                "B4": flightline[8],
                "A5": flightline[9],
                "B5": flightline[10],
            }
        else:
            passengers[flightline[0]] = {
                "A1": flightline[1],
                "B1": flightline[2],
                "C1": flightline[3],
                "A2": flightline[4],
                "B2": flightline[5],
                "C2": flightline[6],
                "A3": flightline[7],
                "B3": flightline[8],
                "C3": flightline[9],
                "A4": flightline[10],
                "B4": flightline[11],
                "C4": flightline[12],
                "A5": flightline[13],
                "B5": flightline[14],
                "C5": flightline[15],
            }
    fileHandle.close()
    return flight


def loadFlight(flight): # loads flights from txt file
    fileHandle = open("flights.txt", "r")  # reads text file
    for line in fileHandle:
        flightline = line[:-1].split("<#>")  # splits each item followed by <#>
        flight[flightline[0]] = {
            "Aircraft": flightline[1],
            "DepLoc": flightline[2],
            "DesLoc": flightline[3],
            "DepDate": flightline[4],
            "DepTime": flightline[5],
            "EstDateArr": flightline[6],
            "EstTimeArr": flightline[7],
            "MaxPass": flightline[8],
        }
    fileHandle.close()
    return flight


def startUp(flight, passengers):
    loadFlight(flight)  # loads previous file with flight records
    loadPassenger(passengers) # loads prev file with passenger records
    print(".*. ⋆. *. Welcome to Lasheep Booking Services! *. ⋆. *. ⋆")
    while 1:
        print(
            "\nWould like to ask if you're an admin or a passenger.\n"
            "[1] - Admin\n[2] - Passenger\n[0] - Exit Program"
        )
        choice = input("Enter Choice: ")
        if choice == "1":
            adminControl(flight, passengers)
        elif choice == "2":
            passengerControl(passengers)
        elif choice == "0":
            print(">>> Thank you for using Lasheep Booking Services! <<<")
            break
        else:
            print(">>> Wrong Input! Please try again. <<<")


startUp(flight, passengers) # main function call for the app


"""
DOCUMENTATION

SPECS CHECKLIST:
    > All records should be saved and loaded in text files - ✓
        - loadFlight(flight) & loadPassengers(passengers)
        - saveFlight(flight) & savePassengers(passengers)
    > ArrivalTime must not be before DepTime - ✓
        - checkAircraftAvailability(flight, name, depdate, deptime, esttimearr)
        - checks if esttime arr is before deptime

ADMIN:
--- adminControl(flight, passengers) ---

    > Add Flight
        === addFlight(flight) ===
        - DepTime should be before ArrTime - ✓ 
        - Conflict of the Same Aircraft - ✓
            > checkAircraftAvailability()

    > Edit Flight - ✓
        === editFlight(flight) ===
        - selected whole details to be edited

    > Delete Flight - ✓
        === delFlight(flight) ===

    > View Flight 
        === viewFlight(flight) ===
        - Sorted by Dep Time - ✓ 
            === depTimeView(flight) ===
        - Departure Location - ✓
            === depLocView(flight) ===
        - Aircraft Name - ✓
            === nameView(flight) ===

    > Search Flight
        === searchFlight(flight) ===
        - Available Seats - ✓
            === tabulateSeats(flight, passengers) ===
        - All flight of an aircraft - ✓
            === searchAircraft(flight) ===
        - All flight of a day - gets na M-Sun isesearch
            === searchDay(flight) ===

PASSENGER:
--- passengerControl(passengers) ---

    > View Flight
    === viewFlight2(flight) ===
        - View all flights sorted by DepTime - ✓
            === depTimeView(flight) === 
        - View all flights using DepLoc - ✓
            === depLocView(flight) ===
        - View flight using DepLoc and DestLoc - ✓, all flights nalang since onti naman
            === depdesLoc(flight) ===

    > Book Flight
    === addPassenger(passengers) ===
        - Select Flight ID - ✓
        === choice is taken through tabulateSeats() function ==
        - Once selected, choose seat (A1, B1..), ask for name - ✓
            === replaces name in dictionary === 
        - Tabulated seat show - ✓
            === tabulate module below ==

* Tabular dapat viewing of seats (2x5 or 3x5) - ✓ (tabulate module)
A1 B1           A1 B1 C1
A2 B2           A2 B2 C2
.. ..           .. .. ..

Went for a minimalistic approach, since I don't have knowledge in GUI yet. xD

==== FINAL PROJECT / RebberChicken ====
Date Started: 12/31/21 - 10:30 AM
Date Ended: 01/11/21 - 11:45 AM

"""
