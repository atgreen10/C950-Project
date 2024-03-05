import csv
import HashTable

class Package:

    def __init__(self, packageID, packageAddress, city, state, postalCode, timeDelivered, deliveryStat):
        self._packageID = packageID
        self._packageAddress = packageAddress
        self._city = city
        self._state = state
        self._postalCode = postalCode
        self.deliveryStat = deliveryStat
        self.timeDelivered  = timeDelivered

    def getPackageId(self):
        return self._packageID

    def getAddress(self):
        return self._packageAddress

    def getCity(self):
        return self._city

    def getState(self):
        return self._state

    def getPostalCode(self):
        return self._postalCode

    def setDeliveryStatus(self, status):
        self.deliveryStat = str(status)

    def getDeliveryStat(self):
        return self.deliveryStat

    def getTimeDelivered(self):
        return self.timeDelivered

    def setTimeDelivered(self, time):
        self.timeDelivered = time


# this formats display of info when the object is printed to the console.
    def __str__(self):
        return self.getPackageId() + " " + self.getAddress() + " " + self.getCity() + " " + self.getState() + " " \
               + self.getPostalCode() + " " + str(self.getDeliveryStat()) + " " + str(self.getTimeDelivered())

    # def __repr__(self):
    #     return self.getPackageId() + " " + self.getAddress() + " " + self.getCity() + " " + self.getState() + " " \
    #            + self.getPostalCode() + " " + self.getDeliveryStat()

# Reads CSV File for package info
with open('packageCSV.csv') as packageFile:
    packageCSV = csv.reader(packageFile, delimiter=',')

    # Creates hashtable object to load package info to
    myHash = HashTable.HashTable()

    # Parse CSV for package info and creates object.
    for row in packageCSV:
        packageID = row[0]
        packageAddress = row[1]
        city = row[2]
        state = row[3]
        postalCode = row[4]
        deliveryStat = " "
        deadLine = row[5]
        weight = row[6]
        notes = row[7]
        timeDelivered = ""
        lastLocationMileage = 0
        packageObj = Package(packageID, packageAddress, city, state, postalCode, deliveryStat,
                                      timeDelivered)
        key = packageID
        value = packageObj

    #  Stores object in hash table
        myHash.insert(int(packageObj.getPackageId()), packageObj)

      # print hash table for verification
      #   for i in range(1, 41):
      #        print(myHash.get(i))
