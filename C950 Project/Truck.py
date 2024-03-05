

class Truck:
    def __init__(self, departureTime = None, currentLocation = '4001 South 700 East', totalDistance = 0.0,
                 destinationLocation = None):
        self.packagesOnTruck = []
        self.departureTime = departureTime
        self.currentLocation = currentLocation
        self.totalDistance = totalDistance
        self.optimizedList = []
        self.destinationLocation = destinationLocation
        self.timeTraveled = 0
        self.updatedTimes = 0
        self.hubLocation = '4001 South 700 East'
        self.updatedTimesList = []

    def loadPackage(self, package):
        self.packagesOnTruck.append(package)

    def getTotalDistance(self):
        return self.totalDistance

    def getPackageList(self):
        return self.packagesOnTruck

    def getCurrentLocation(self):
        return self.currentLocation

    def getPackageID(self, index):
        return self.getPackageList().index(index)

    def getPackageAddress(self, packageID):
        for package in self.getPackageList():
            if package.getPackageId() == str(packageID):
                return package.getAddress()

    def getOptimizedList(self):
        return self.optimizedList

