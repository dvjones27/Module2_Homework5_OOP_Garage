class Vehicle:
    
    # self.licensePlate = licensePlate
    
    def __init__(self, licensePlate, vehicleType, make, model, color):
        self.licensePlate = licensePlate
        self.vehicleType = vehicleType
        self.make = make
        self.model = model
        self.color = color
    
    def __repr__(self):
        return f'{self.licensePlate}, {self.vehicleType},  {self.make}, {self.model}, {self.color}' 

    def license(self):
        return self.licensePlate



class parkingGarage():
    def __init__(self):
        self.vehiclesAdded = []
        self.parkingSpaces = 100
        self.vehicleInfo = {}
        self.tickets = 10000
        self.currentTicket = "" 
        self.payment = 0
        # self.licensePlate = license.licensePlate
              
    def spacesAvailable(self):
        return self.parkingSpaces
    
    def ticketsAvailble(self):
        if self.currentTicket[value] == 0:
            return "Paid"
        else:
            return "Not Paid"
        return self.tickets, 
    
    def addVehicle(self, vehicle):
        
        if self.parkingSpaces > 0:
            self.vehiclesAdded.append(str(vehicle).split(', ')) 
            self.currentTicket += str(1)        
            self.parkingSpaces -= 1
            self.tickets -= 1            
            self.vehicleInfo = {'Code': [], 'Vehicle Type': [], 'License Plate': [], 'Make': [], 'Model': [], 'Color': []} 
            
            for index, i in enumerate(self.vehiclesAdded):
                
                self.vehicleInfo['Code'].append(self.currentTicket[index])
                self.vehicleInfo['License Plate'].append(i[0])
                self.vehicleInfo['Vehicle Type'].append(i[1])
                self.vehicleInfo['Make'].append(i[2])
                self.vehicleInfo['Model'].append(i[3])
                self.vehicleInfo['Color'].append(i[4])
            return "Vehicle successfully added to the Parking Garage"        
        else:            
          print(f"We have {self.parkingSpaces} spaces available. Please check back later.")

    def removeVehicle(self, codeInfo, billTime):
        
        codeEntry = (self.vehicleInfo['Code']) 
        if codeEntry not in self.vehicleInfo['Code']:
            print("We could not find your car. Are you sure you parked your car here? ")        
        else:
            
            for i, v in enumerate(self.vehicleInfo['Code']):
                if v == codeEntry:
                    
                    print("Your Vehicle's License Plate is: ",
                          self.vehcileInfo['License Plate'][index])
                    print("Your Vehicle's Type is: ",
                          self.vehcileInfo['Vehicle Type'][index])
                    print("Your Vehicle's Make is: ",
                          self.vehcileInfo['Make'][index])
                    print("Your Vehicle's Model is: ",
                           self.vehicleInfo['Model'][index])
                    print("Your Vehicle's Color is: ",
                           self.vehicleInfo['Color'][index]) 
                    removedVehicleIndex = self.vehicleInfo['Code'].pop(index)
                    self.vehicleInfo['License Plate'].pop(index)
                    self.vehicleInfo['Vehicle Type'].pop(index)
                    self.vehicleInfo['Make'].pop(index)
                    self.vehicleInfo['Model'].pop(index)
                    self.vehicleInfo['Color'].pop(index)                    
                    self.parkingSpaces          
                    self.parkingSpaces += 1
        if len(self.vehicleInfo['Code']) < codeEntry:
            while True:
                if billTime.isnumeric():
                    
                    timeCode = [billTime, removeVehicle]
                    break              
                else:                    
                    print("Your input must be an integer. Example:  input: 5.")     
                billTime = input("Enter how long you were in the parking garage in hours or 'q' to quit. Example input: 5.")               
                if billTime in ['q', 'Q']:                    
                    break 
                self.payment = int(timeCode[0]) * 5
                return f'Your Total payment is: ${self.payment}.'
            else:                
                self.payment = int(timeCode[0]) * 5 + 100
                return f'Your Total Payment is: ${self.payment}.' 
    def vehiclesParked(self):
        for i in self.vehicleInfo.items():                
            print(i)
                    
# class payForParking():
#     def __init__(self):
    
# class leaveGarage():
#     def __init__(self):

parkingGarage = parkingGarage()
print(f'The number of Parking Spaces are: {parkingGarage.spacesAvailable()}.')
parkingGarage.addVehicle(Vehicle('L34VG34', 'Sedan', 'Honda', 'Accord', 'Red'))
parkingGarage.addVehicle(Vehicle('U21TEV3', 'Coupe', 'Porsche', 'Carrera', 'Blue'))
parkingGarage.addVehicle(Vehicle('H97VG34', 'Motorcycle', 'Ducati', 'Panigale V4', 'Red'))
# parkingGarage.vehiclesParked()
# print(takeTicket.ticketsAvailable())
print(f'The number of Current Parking Spaces Available are: {parkingGarage.spacesAvailable()}.')
# print(f'Time to Pay for Parking: {payForParking()}.')


# print(parkingGarage.billTime())

# print(f"The total parking spaces in the garage are: {parkingGarage.parkingSpaces()}")

# print(f"There are {parkingGarage.currentParkingTickets} cars in the garage.")
# fancyGarage.takeTicket(1)
# print(f"The available parking spaces in the garage: {fancyGarage.currentParkingSpaces_available}")

# print(parkingGarage.parkingTime)
# print(parkingGarage.TotalTime)
# print(parkingGarage.payForParking())


# while True:
#     if fancyGarage.currentTickets > 0:
#         giveTicket = (f"Please take ticket. There are {fancyGarage.parkingSpacesAvailable()} parking spaces. Stay safe and park well!")
#     else:
#         print(f"I do apologize but there are {fancyGarage.self.currentParkingSpaces} parking spaces. It looks like we do not have any parking spaces left.")

# ClearData()
  
    # if question.lower() == "add":
    #     NewFeatures.addCartItems()
    # elif question.lower() == "delete":
    #     NewFeatures.deleteCartItems()
    # elif question.lower() == "show":
    #     NewFeatures.showCartItems()
    # elif question.lower() == "quit":
    #     NewFeatures.quit()
    # else:
    #     break








# class Cart():
    
            
#     def __init__(self, items, totalItems = {}):
#         self.items = items
#         self.totalItems = totalItems
     
        
#     def addCartItems(self):
#         addItems = input("What would you like to add? ")
#         addPrice = float(input("What is the cost of this item? "))
#         self.totalItems[addItems] = addPrice
#         endAdd = input("Would you like to add more? ")
#         if endAdd.lower() == "yes":
#             NewFeatures.addCartItems()
            
#     def deleteCartItems(self):
#         deleteItems = input("What would you like to delete?")
#         del self.totalItems[deleteItems]
#         endDelete = input("Would you like to delete more?")
#         if endDelete.lower() == "yes":
#             NewFeatures.deleteCartItems()
                    
                    
#     def showCartItems(self):
#         [print(k, " : ", v) for k, v in self.totalItems.items()]
#         print(f"The length of the shopping list is: {len(self.totalItems.keys())} \nThe total sum of items is:  ${sum(self.totalItems.values()):.2f}") 

            
#     def quit(self):
#         [print(k, " : ", v) for k, v in self.totalItems.items()]
#         print(f"The length of the shopping list is: {len(self.totalItems.keys())} \nThe total sum of items is:  ${sum(self.totalItems.values()):.2f}")


# NewFeatures = Cart({})

# while True:
#     question = input("Do you want to : Show/Add/Delete or Quit? ")
#     if question.lower() == "add":
#         NewFeatures.addCartItems()
#     elif question.lower() == "delete":
#         NewFeatures.deleteCartItems()
#     elif question.lower() == "show":
#         NewFeatures.showCartItems()
#     elif question.lower() == "quit":
#         NewFeatures.quit()
#     else:
#         break











# def addVehicle(self, vehicle):
   # def takeTicket():
        # - This should decrease the amount of tickets available by 1
        # - This should decrease the amount of parkingSpaces available by 1
        
    #     numOfTickets()
    #     parkingSpaces()
    # def payForParking():
        # - Display an input that waits for an amount from the user and store it in a variable
        # - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
        # # - This should update the "currentTicket" dictionary key "paid" to True
        # amountDue()
        # hasTicketBeenPaid()
        # totalDue()
        # paymentAmount()
        
        
        
    # def leaveGarage():
        # - If the ticket has been paid, display a message of "Thank You, have a nice day"
        # - If the ticket has not been paid, display an input prompt for payment
        # - Once paid, display message "Thank you, have a nice day!"
        # - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # - Update tickets list to increase by 1 (meaning add to the tickets list)
        
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary


# class parkingGarage:
     
# # Class Constructor with four attributes 
#     def __init__(self):
#         # self.items = items
#         # self.cars_added = []        
#         # self.parkingSpaces = []       
#         # self.car_info = {} 
#         self.tickets = []
#         self.currentTicket = {}      
#         self.bill = 0
#         # self.totalTime = 0
#     # this function returns the number of spots availables
#     # The add_car function adds a car to the parking lot
#     # It takes one input parameter
#     # That input parameter are the license plate, Model and Color
#     def takeTicket(self): #Required
        
#         self.currentTicket += 1
#         self.parkingSpaces += 1
        
#     def parkingSpacesAvailable(self):
#         self.parkingSpaces += 1
#         return self.parkingSpacesAvailable
    
#     def currentParkingTickets(self):
#         self.currentTickets += 1 
#         return self.currentTickets
    
#         if parkingSpacesAvailable() > 0 and self.tickets > 1:
#             self.parkingSpaces -= 1
#             self.tickets -= 1
#             self.currentTickets += 1 
#             print(f"Welcome the Parking Garage! We are happy to have you as we have {self.parkingSpaces - self.currentParkingTickets} parking spaces available.")
#         else:            
#           print(f"We have {self.parkingSpots} parking spots available. I do apologize, we do not have any parking spots available. ")
#     # def currentParkingSpaces_available(self):
#     #     self.currentParkingSpaces_available = self.parkingSpaces - self.currentTickets
#     #     return self.currentParkingSpaces_available
    
#     # def parkingTime(self):
#     #     entTime = datetime.now()
#     #     entTimeFormat = entTime.strftime("%d-%m-%Y at %H:%M:%S")
#     #     startdate=datetime.ctime
        
#     #     self.entryTime = entTimeFormat #ctime(entTime)
#     #     # randNum = random.randrange(1,12)
#     #     extTime = datetime.now()
#     #     self.exitTime = extTime.strftime("%d-%m-%Y at %H:%M:%S")
        
#     #     self.totalTime = str(self.exitTime - self.entryTime)
        
#     #     print(f"The entry time was: {self.entryTime}")
#     #     print(f"The exit time is: {self.exitTime}")
#     #     # print(f"The total parking time is: {self.totalTime}")

#     #     return  self.entryTime, self.exitTime, self.totalTime
    
#     def payForParking(self): #Required
#         # self.DateTime = self.getTime()
        
        
#         def getTime(self):
#             addTime = random.randint(1,12)
#             entTime = datetime.now() - timedelta(hours=addTime) - timedelta(minutes=addTime) - timedelta(milliseconds=addTime)
#             entTime = entTime.strftime("%d-%m-%Y at %H:%M:%S")
#             extTime = datetime.now()
#             self.exitTime = extTime.strftime("%d-%m-%Y at %H:%M:%S")
            
#             self.totalTime = str(self.exitTime - self.entryTime)
            
#             print(f"The entry time was: {self.entryTime}")
#             print(f"The exit time is: {self.exitTime}")
#             return self.entryTime, self.exitTime, self.totalTime
        
        
#         def amountDue():
            
#             return
        
#         def hasTicketBeenPaid():
            
#             return
        
#         def totalDue():
            
#             return
        
#         def currentParkingTicket():
#             currentTicket -= 1
            
#             return
            
#         def paymentAmount():
            
#             # print(f"The total parking time is: {self.totalTime}")
#             return
        
#         # return (self.totalTime * 3)
    
#     def leaveGarage(self): #Required
#         if self.totalTime >= 60:
#             print(f"Thank you for parking with us for {self.totalTime} hours. \nHave an awesome day!")
#         else:
#             print(f"Thank you for parking with us for {self.totalTime} minutes. \nHave an awesome day!")
    
        
#             while True:
                
#                 if self.totalTime.isnumeric():
                    
                    
#                     break            
#                 else:                    
#                   print("Your input must be an integer. Sample input: 5 ")
#                 bill_hours = input("Enter for how long you were on the parking lot in hours or 'q' to quit. Example input: 5  -->  ")
#                 if bill_hours in ['q', 'Q']:                     
#                     break
#             self.parkingSpaces += 1
#     # displays all cars in garage
#     # def cars_in_garage(self): 
# # creating instances of each class
