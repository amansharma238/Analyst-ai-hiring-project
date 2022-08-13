from ast import Return


vehicles = {'bikes':2,'cycle':3,'car':1,'boat':2} # {‘vehicle_type’: inventory}
customers = []
bookings = []

class Customer:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
    def display(self):
        print(f'Name: {self.name} Phone Number: {self.phone_number} Email: {self.email}')

    def getCustomer(self):
        customer = {'CustomerName': self.name, 'PhoneNmber': self.phone_number, 'Email': self.email}
        return customer

class RentalBooking:
    def __init__(self, customer_name, rental_date, return_date, vehicle_type):
        self.customer_name = customer_name
        self.rental_date = rental_date
        self.vehicle_type = vehicle_type
        self.return_date = return_date
    
    def display(self):
        print(f'Name: {self.customer_name}, rental__date: {self.rental_date}, return date: {self.return_date}, vehicle_type: {self.vehicle_type}')


def main():
    is_exit = False
    while not is_exit:
        print("""What you want: 
1. Add customer
2. Add rental booking
3. See customer list
4. See rental booking list
5. See inventory of vehicles available
6. exit""")
        option = input()
        if (option == '1'):
            add_customer()
        elif (option == '2'):
            add_rental_booking()
        elif (option == '3'):
            show_customers_list()
        elif (option == '4'):
            show_rental_list()
        elif (option == '5'):
            show_inventory_of_vehicles()
        elif (option == '6'):
            is_exit = True
        else:
            print('\nEnter Valid option...\n')

def add_customer():
    print('\nEnter Customer details')
    CustomerName = input('Enter Name: ')
    PhoneNumber = input('Enter Phone Number: ')
    Email = input('Enter Email: ')
    customer = Customer(CustomerName,PhoneNumber, Email)
    customers.append(customer)
    print('\n------ Customer Added Successfully ------\n')

def add_rental_booking():
    print('Enter Details: \n')
    print('Enter customer detail from below list:')
    show_customers_list()
    CustomerName = input('Enter customer name: ')
    is_customer_present = False
    for customer in customers:
        if customer.getCustomer()['CustomerName'] == CustomerName:
            is_customer_present = True
            break
    if not is_customer_present:
        print('\nSorry no customer found in data..(Also strings are case sensitive)\n')
        return
    RentalDate = input('Enter Rental Date: ')
    ReturnDate = input('Enter return date (if returned otherwise leave blank): ')
    print('select vehicle type from below list')
    show_inventory_of_vehicles()

    vehicle = input('Enter vehicle type: ')

    is_vehicle_there = False
    for v in vehicles:
        if vehicle == v:
            is_vehicle_there = True
            break

    if not is_vehicle_there:
        print(f'\nsorry {vehicle} is not there in vehicles list\n')    
        return
    if vehicles[vehicle]<=0:
        print(f'\n{vehicle} cannot be rented as it is already booked\n')
        return
    
    vehicles[vehicle]  -= 1   
    rental_booking = RentalBooking(CustomerName,RentalDate,ReturnDate,vehicle);
    bookings.append(rental_booking)
    print('\n---- Booking done Successfully ----\n')


def show_customers_list():
    if len(customers) ==0:
        print('\nSorry No data available.\n')
    for customer in customers:
        print('\n')
        customer.display()
        print('\n')

def show_rental_list():
    if len(bookings)==0:
        print('\nSorry No data available.\n')
    for rental_item in bookings:
        print('\n')
        rental_item.display()
        print('\n')

def show_inventory_of_vehicles():
    print('\n')
    for i in vehicles:
        print(f'Vehicle Type: {i}, Inventory: {vehicles[i]}')
    print()


if __name__ == '__main__':
    main()
    