# Austin Green      Student ID: #000946771
from copy import copy

import HashTable
import csv
import datetime
import distance
import Package
import Truck


# Implements truck1 object
truck1 = Truck.Truck()
truck1.departureTime = datetime.timedelta(hours = 8, minutes = 0)
truck1.totalTime = datetime.timedelta()
truck1.firstTrip = []
# print(truck1.departureTime)

# Implements truck2 object
truck2 = Truck.Truck()
truck2.departureTime = datetime.timedelta(hours = 9, minutes = 5)
truck2.totalTime = datetime.timedelta()
# print(truck2.departureTime)

# append 16 packages to truck1
truck1.loadPackage(Package.myHash.get(1))
truck1.loadPackage(Package.myHash.get(5))
truck1.loadPackage(Package.myHash.get(6))
truck1.loadPackage(Package.myHash.get(13))
truck1.loadPackage(Package.myHash.get(14))
truck1.loadPackage(Package.myHash.get(15))
truck1.loadPackage(Package.myHash.get(16))
truck1.loadPackage(Package.myHash.get(19))
truck1.loadPackage(Package.myHash.get(20))
truck1.loadPackage(Package.myHash.get(21))
truck1.loadPackage(Package.myHash.get(27))
truck1.loadPackage(Package.myHash.get(29))
truck1.loadPackage(Package.myHash.get(33))
truck1.loadPackage(Package.myHash.get(34))
truck1.loadPackage(Package.myHash.get(35))
truck1.loadPackage(Package.myHash.get(39))

# Creates a copy of all packages in the first trip so it can be compared later when we search for all packages at a
# specific time. This allows us to check whether tha package is in transit or at the hub still.
truck1.firstTrip = truck1.packagesOnTruck.copy()

# marks the loaded packages as "In transit"
for i in truck1.packagesOnTruck:
    i.deliveryStatus = "In transit"

# appends 16 packages to truck2
truck2.loadPackage(Package.myHash.get(3))
truck2.loadPackage(Package.myHash.get(12))
truck2.loadPackage(Package.myHash.get(4))
truck2.loadPackage(Package.myHash.get(8))
truck2.loadPackage(Package.myHash.get(10))
truck2.loadPackage(Package.myHash.get(30))
truck2.loadPackage(Package.myHash.get(18))
truck2.loadPackage(Package.myHash.get(25))
truck2.loadPackage(Package.myHash.get(26))
truck2.loadPackage(Package.myHash.get(28))
truck2.loadPackage(Package.myHash.get(31))
truck2.loadPackage(Package.myHash.get(32))
truck2.loadPackage(Package.myHash.get(36))
truck2.loadPackage(Package.myHash.get(37))
truck2.loadPackage(Package.myHash.get(38))
truck2.loadPackage(Package.myHash.get(40))

# marks packages as in transit once loaded.
for j in truck2.packagesOnTruck:
    j.setDeliveryStatus = "In transit"

# loop through truck1.optimized list to get truck1.destinationLocation, run distance.checkDistance function with
# truck1.currentLocation to get distance between the two and update truck1.totalDistance then update
# truck1.currentlocation. Run again with next package in the list. calculate the time it takes to go to each location

truck1.optimizedList = distance.optimizeList(truck1)
# print('truck1 list :', truck1.optimizedList)
truck1.updatedTimes = truck1.departureTime
truck1.updatedTimesList = []
truck1.currentLocation = truck1.hubLocation

# this is where the truck "travels" and time of deliveries and distances traveled is calculated. Only single 'for' loop
# used so time complexity is still O(N^2)
for i in truck1.optimizedList:
    #travelTime in seconds
    travelTime = ((distance.timeToTravel(truck1.currentLocation, i.getAddress()) * 60)*60)
    truck1.updatedTimes = truck1.updatedTimes + datetime.timedelta(seconds = travelTime)
    # list of updated times for each package.
    truck1.updatedTimesList.append(truck1.updatedTimes)
    # print(truck1.updatedTimes)
    i.setTimeDelivered(truck1.updatedTimes)
    i.deliveryStat = "Delivered"
    print(i)
    # print('time of delivery for package ' + i.__str__() + ' is ' + str(i.timeDelivered))
    Package.myHash.update(i.getPackageId(), i)
    # print('Updated Package in hashTable: ', Package.myHash.get(i.getPackageId()))
    distBetweenCurrentAndDest = distance.checkDistance(truck1.currentLocation, i.getAddress())
    truck1.currentLocation = i.getAddress()
    truck1.totalDistance = float(truck1.totalDistance) + float(distBetweenCurrentAndDest)
    # print(i)
    # Package.myHash.get(int(i.getPackageId()))
# print('total distance for truck1 is: ', truck1.totalDistance)
    # print('distance between: ' + str(distBetweenCurrentAndDest) + ' and total distance: ' + str(truck1.totalDistance))

# variable set up to pull the final package delivery time to continue keeping track of the time when returning to hub
# to pick up other packages.
# finalTime = truck1.updatedTimesList[len(truck1.updatedTimesList) - 1]
# + truck2.updatedTimesList[len(truck2.updatedTimesList)]
# print(finalTime)

# Loop thru truck2.optimized list and get truck2.destinationLocation, run distance.checkDistance with
# truck2.currentLocation and get distance between the two locations. Update truck2.totalDistance and
# truck2.currentLocation. calculate the time it takes to go to each location and change the delivery status

truck2.optimizedList = distance.optimizeList(truck2)
# print('truck2 list :')
# print(truck2.optimizedList)
truck2.updatedTimes = truck2.departureTime
truck2.updatedTimesList = []
truck2.currentLocation = truck2.hubLocation


for j in truck2.optimizedList:
    # travelTime in seconds
    travelTime = ((distance.timeToTravel(truck2.currentLocation, j.getAddress()) * 60) * 60)
    truck2.updatedTimes = truck2.updatedTimes + datetime.timedelta(seconds = int(travelTime))
    truck2.updatedTimesList.append(truck2.updatedTimes)
    # print(truck2.updatedTimes)
    j.setTimeDelivered(truck2.updatedTimes)
    j.deliveryStat = 'Delivered'
    print(j)
    # print('travel time between ', truck2.currentLocation, ' and ', j.getAddress(), ' is ', travelTime, ' minutes')
    # print('time of delivery for package ' + j.__str__() + ' is ' + str(j.timeDelivered))
    distanceFromCurrentLocation = distance.checkDistance(truck2.currentLocation, j.getAddress())
    truck2.currentLocation = j.getAddress()
    truck2.totalDistance = truck2.totalDistance + float(distanceFromCurrentLocation)
    # Package.myHash.get(int(j.getPackageId()))
# print('truck 2 total distance before the if statement: ', truck2.totalDistance)

# finalTime = truck1.updatedTimesList[len(truck1.updatedTimesList) - 1] + truck2.updatedTimesList[len(
#     truck2.updatedTimesList) - 1]

# Checks which truck is closer to the hub to make the second trip
truck1Dist = distance.checkDistance(truck1.currentLocation, truck1.hubLocation)
truck2Dist = distance.checkDistance(truck2.currentLocation, truck2.hubLocation)
# print(truck1Dist)
# print(truck2Dist)

# print('truck1Dist is ', truck1Dist)
# print('truck2Dist is ', truck2Dist)

# Situation if truck 1 is closer to hub than truck2
if truck1Dist < truck2Dist:
    truck1.totalDistance += truck1Dist
    # time to add to total in seconds from current location back to hub for last packages.
    timeToHub = (((truck1Dist / 18) * 60) * 60)
    truck1.updatedTimes = truck1.updatedTimes + datetime.timedelta(seconds = timeToHub)

    # clears truck1's packages list and optimized list to keep track of second trip's packages
    truck1.optimizedList = []
    truck1.packagesOnTruck = []

# truck1's second trip packages.
    truck1.loadPackage(Package.myHash.get(2))
    truck1.loadPackage(Package.myHash.get(7))
    truck1.loadPackage(Package.myHash.get(9))
    truck1.loadPackage(Package.myHash.get(11))
    truck1.loadPackage(Package.myHash.get(17))
    truck1.loadPackage(Package.myHash.get(22))
    truck1.loadPackage(Package.myHash.get(23))
    truck1.loadPackage(Package.myHash.get(24))

    # marks the packages on truck1 as in transit.
    for items in truck1.packagesOnTruck:
        items.deliveryStat = "In Transit"

    # Optimized the list of packages using nearest neighbor algorithm.
    truck1.optimizedList = distance.optimizeList(truck1)
    # truck1.updatedTimes = finalTime
    # print(truck1.optimizedList)

    # Uses optimized list of packages to start delivering and keeping track of location, times, and total distances.
    for i in truck1.optimizedList:
        travelTime = ((distance.timeToTravel(truck1.currentLocation, i.getAddress()) * 60) * 60)
        truck1.updatedTimes = truck1.updatedTimes + datetime.timedelta(seconds=travelTime)
        truck1.updatedTimesList.append(truck1.updatedTimes)
        i.setTimeDelivered(truck1.updatedTimes)
        i.deliveryStat = "Delivered"
        print(distance.checkDistance(truck1.currentLocation, i.getAddress()))
        distBetweenCurrentAndDest = distance.checkDistance(truck1.currentLocation, i.getAddress())
        truck1.currentLocation = i.getAddress()
        truck1.totalDistance = truck1.totalDistance + float(distBetweenCurrentAndDest)

        # if truck2Distance is close to the hub after delivering all packages, truck2 goes back to hub to pick up
        # rest of packages.
else:
    # truck2.updatedTimes = finalTime
    # truck2.totalDistance += truck2Dist
    # time to add to total in seconds from current location back to hub for last packages.
    timeToHub = (((truck1Dist / 18) * 60) * 60)
    truck2.updatedTimes = truck2.updatedTimes + datetime.timedelta(seconds=timeToHub)
    truck2.optimizedList = []
    truck2.packagesOnTruck = []

    truck2.loadPackage(Package.myHash.get(2))
    truck2.loadPackage(Package.myHash.get(7))
    truck2.loadPackage(Package.myHash.get(10))
    truck2.loadPackage(Package.myHash.get(11))
    truck2.loadPackage(Package.myHash.get(17))
    truck2.loadPackage(Package.myHash.get(22))
    truck2.loadPackage(Package.myHash.get(23))
    truck2.loadPackage(Package.myHash.get(24))

    for items in truck2.packagesOnTruck:
        items.deliveryStat = "In Transit"

    truck2.optimizedList = distance.optimizeList(truck2)
    # print(truck2.updatedTimes)
    for i in truck2.optimizedList:
        travelTime = ((distance.timeToTravel(truck2.currentLocation, i.getAddress()) * 60) * 60)
        # truck2.updatedTimes = finalTime + datetime.timedelta(seconds=travelTime)
        truck2.updatedTimesList.append(truck2.updatedTimes)
        # print(truck2.updatedTimes)
        i.setTimeDelivered(truck2.updatedTimes)
        i.deliveryStat = "Delivered"
        print(i)
        # print('travel time between ', truck2.currentLocation, ' and ', i.getAddress(), ' is ', travelTime, ' seconds')
        # print('time of delivery for package ' + i.__str__() + ' is ' + str(i.timeDelivered))
        Package.myHash.update(i.getPackageID, i)
        # print('Updated Package in hashTable: ', Package.myHash.get(i))
        distBetweenCurrentAndDest = distance.checkDistance(truck2.currentLocation, i.getAddress())
        truck2.currentLocation = i.getAddress()
        truck2.totalDistance = truck2.totalDistance + float(distBetweenCurrentAndDest)

distanceTotal = truck1.totalDistance + truck2.totalDistance
truck1Time = truck1.updatedTimes - truck1.departureTime
truck2Time = truck2.updatedTimes - truck2.departureTime




print('         Welcome to WGUPS Package Tracker')
print('----------------------------------------------------------')
# print('The current route was completed at ', str(finalTime), ' with a total distance of ', str(distanceTotal), ".")
print('Truck 1 drove a total of ', str(truck1.totalDistance), ' miles in ', truck1Time)
print('Truck 2 drove a total of ', str(truck2.totalDistance), ' miles in ', truck2Time)
print('Truck 3 was not in service today.')
print('Total mileage was ', str(distanceTotal))
print('What would you like to do?')
print('[A]: Lookup specific package information.    [B]: Look up all packages at a specific time')

userInput = str(input('Enter the letter for your selection: '))

if userInput == 'A' or userInput == 'a':
    userInputA = int(input('Please enter the package number you would like to lookup: \n'))
    print(Package.myHash.get(userInputA))
elif userInput == 'B' or userInput == 'b':
    userInputB = input('Enter a time for your query using HH:mm format:  ')
    (h, m) = userInputB.split(':')
    convertedTime = datetime.timedelta(hours = int(h), minutes = int(m))

    for i in range(1, 41):
        # packageDeliveryTime = Package.myHash.get(i).getTimeDelivered()
        if Package.myHash.get(i).getTimeDelivered() > convertedTime:
            if Package.myHash.get(i) not in truck2.optimizedList and Package.myHash.get(i) not in \
                    truck1.firstTrip:
                Package.myHash.get(i).deliveryStat = 'At Hub'
            else:
                Package.myHash.get(i).deliveryStat = 'In transit'
        else:
            Package.myHash.get(i).deliveryStat = 'Delivered'
        print(Package.myHash.get(i))

