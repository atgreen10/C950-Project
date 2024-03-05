import csv
import Truck

from HashTable import HashTable
# Reads CSV file for distance info
with open('Distance.csv') as distanceFile:
    distanceCSV = csv.reader(distanceFile, delimiter=',')
    distanceTable = []
    for row in distanceCSV:
        distanceTable.append(row)
   # print(distanceTable)

# reads csv file for address info
with open("addressTable.csv") as addressFile:
    addresses = [','.join(row) for row in csv.reader(open("addressTable.csv"), delimiter=',')]
    #print(addresses)


    def checkDistance(currentLocation, destinationLocation):
        indexCurrent = addresses.index(currentLocation)
        for address in addresses:
            if destinationLocation == address:
                indexDest = addresses.index(destinationLocation)
                if distanceTable[indexCurrent][indexDest] == '':
                    distance = float(distanceTable[indexDest][indexCurrent])
                else:
                    distance = float(distanceTable[indexCurrent][indexDest])
                return distance

# Selection sort algorithm is used to find the package considered to be the 'nearest neighbor' based on the truck's
    # current location
    def optimizeList(Truck):
        lowestDist = 30.0
        temp = None
        packageList = Truck.getPackageList()
        numOfPkgs = len(Truck.packagesOnTruck)-1
        optimizedList = Truck.getOptimizedList()
        while len(Truck.optimizedList) <= numOfPkgs:
            for package in packageList:
                dist = float(checkDistance(Truck.getCurrentLocation(), package.getAddress()))

                if dist <= lowestDist:
                    temp = package
                    lowestDist = dist
            optimizedList.append(temp)
            Truck.currentLocation = temp.getAddress()
            lowestDist = 30.0
            if temp in packageList:
                packageList.remove(temp)
        return optimizedList

# find the time it takes the truck to travel the distance between its current location and the package address and
    # returns time in miles per hour.
    def timeToTravel(start, end):
        truckSpeed = 18.0
        travelTime = (checkDistance(start, end) / truckSpeed)
        return travelTime
