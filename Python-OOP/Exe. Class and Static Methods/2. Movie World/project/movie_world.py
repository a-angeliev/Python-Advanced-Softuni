from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for cust in self.customers:
            if cust.id == customer_id:
                customer = cust
        for dv in self.dvds:
            if dv.id == dvd_id:
                dvd = dv

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            else:
                return "DVD is already rented"
        else:
            if dvd.age_restriction > customer.age:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
            else:
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for cust in self.customers:
            if cust.id == customer_id:
                customer = cust
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                dvd = dvd
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        string = ''
        for el in self.customers:
            string += f"{el}\n"
        for el in self.dvds:
            string += f"{el}\n"
        return string

a = MovieWorld("tata")
a.add_customer(4)

