class parkingGarage():
    
    def __init__(self):
        self.tickets = [1000]
        self.parkingSpaces = [30]
        self.currentTicket = {}
        self.currentTicket['paid'] = False
        
        print(f"Thank you for using The Parking Garage. \nThere are {str(self.parkingSpaces)[1:-1]} spaces available. \nThere are {str(self.tickets)[1:-1]} tickets available.")   
        
    def takeTicket(self):
         
        self.tickets.append(-1)
        self.parkingSpaces.append(-1)
        
        print(f"Here is your ticket.  \nYou have 15 minutes of free parking. \nThere are {sum(self.parkingSpaces)} spaces available. \nThere are {sum(self.tickets)} tickets available.")
          

    def payForParking(self):
        # self.currentTicket['paid'] == True
        
        if self.currentTicket['paid'] == True:
            print(f"Thank You So Much! Your ticket has been paid! \nCurrent Ticket Status: {self.currentTicket['paid']}. Have an Awesome Day! \nThere are {sum(self.parkingSpaces)} available. \nThere are {sum(self.tickets)} tickets available.")
        else:
            # self.currentTicket['paid'] == True
        
            print(f"Current Ticket Status: {self.currentTicket['paid']}. Please enter your card for payment.")
            
            
    def leaveGarage(self):
        
        if self.currentTicket['paid'] == True:
            print(f"Thank You So Much! Your ticket has been paid! \nCurrent Ticket Status: {self.currentTicket['paid']}. Have an Awesome Day! \nThere are {sum(self.parkingSpaces)} available. \nThere are {sum(self.tickets)} tickets available.")
        
        else:
            print(f'How are you making payment? \n1. Cash or \n2. Card?')
            payInput = int(input())
            if payInput == 1:
                print(f"Thank You So Much! Have an Awesome Day! \nThere are {sum(self.parkingSpaces)} available. \nThere are {sum(self.tickets)} tickets available.")                
                
            else:
                print(f"Here is your change. Have an Awesome Day! \nThere are {sum(self.parkingSpaces)} available. \nThere are {sum(self.tickets)} tickets available.")
        
        # Updating Items
        self.currentTicket['paid'] = False
        self.parkingSpaces.append(1)
        self.tickets.append(1)       
        print(f"Updated Status.".upper() + f"\nCurrent Ticket Status: {self.currentTicket['paid']}. Have an Awesome Day! \nThere are {sum(self.parkingSpaces)} available. \nThere are {sum(self.tickets)} tickets available.")  
                

parkingGarage = parkingGarage()
print(f'{parkingGarage.takeTicket()}')
print(f'{parkingGarage.payForParking()}')
print(f'{parkingGarage.leaveGarage()}')



# parkingGarage = parkingGarage()
# print()
# print(f'The number of Parking Spaces are: {parkingGarage.spacesAvailable()}.')
# parkingGarage.addVehicle(Vehicle('L34VG34', 'Sedan', 'Honda', 'Accord', 'Red'))
# parkingGarage.addVehicle(Vehicle('U21TEV3', 'Coupe', 'Porsche', 'Carrera', 'Blue'))
# parkingGarage.addVehicle(Vehicle('H97VG34', 'Motorcycle', 'Ducati', 'Panigale V4', 'Red'))
# parkingGarage.vehiclesParked()
# print(takeTicket.ticketsAvailable())
# print(f'The number of Current Parking Spaces Available are: {parkingGarage.spacesAvailable()}.')
# print(f'Time to Pay for Parking: {payForParking()}.')


# print(parkingGarage.billTime())

# print(f"The total parking spaces in the garage are: {parkingGarage.parkingSpaces()}")

# print(f"There are {parkingGarage.currentParkingTickets} cars in the garage.")
# fancyGarage.takeTicket(1)
# print(f"The available parking spaces in the garage: {fancyGarage.currentParkingSpaces_available}")

# print(parkingGarage.parkingTime)
# print(parkingGarage.TotalTime)
# print(parkingGarage.payForParking())

