import sys

class Parking:
    def __init__(self, slots) -> None:
        self.slots = ['-'] * slots
        pass

    def entry(self, vechicle_no, age):
        for i in range(len(self.slots)):
            if self.slots[i] == '-':
                self.slots[i] = [vechicle_no, age]
                return i+1
        return -1
    
    def exit(self, slot_id) -> None:
        res = [self.slots[int(slot_id)]]
        self.slots[int(slot_id)] = '-'
        return res[0]
        pass

    def get_vehicle_by_age(self, age):
        registration_numbers = ''
        for i in self.slots:
            if i == '-':
                continue
            if i[1] == age:
                registration_numbers += i[0]
                registration_numbers += ', '
        
        return registration_numbers[:-2]

    def get_slot(self, registration_number):
        for i in range(len(self.slots)):
            if self.slots[i] == '-':
                continue
            elif self.slots[i][0].strip() == registration_number.strip():
                return i+1
        return -1

    def get_slot_by_age(self, age):
        slots = ''
        for i in range(len(self.slots)):
            if self.slots[i] == '-':
                continue
            if self.slots[i][1] == age:
                slots += str(i+1)
                slots += ','
        
        return slots[:-1]

def __main__():
    parking = None
    for i in sys.stdin:
        i = i.split('\n')[0]
        ip = list(i.split(' '))

        if ip[0] == 'Create_parking_lot':
            parking = Parking(int(ip[1]))
            print('Created parking of {0} slots'.format(len(parking.slots)))

        elif ip[0] == 'Park':
            slot = parking.entry(ip[1],ip[3])
            print('Car with vehicle registration number "{0}" has been parked at slot number {1}'.format(ip[1], slot))

        elif ip[0] == 'Slot_numbers_for_driver_of_age':
            slots = parking.get_slot_by_age(ip[1])
            print(slots)

        elif ip[0] == 'Leave':
            res = parking.exit(ip[1])
            print('Slot number {2} vacated, the car with vehicle registration number "{0}" left the space, the driver of the car was of age {1}'.format(res[0], res[1], ip[1]))
        
        elif ip[0] == 'Vehicle_registration_number_for_driver_of_age':
            registration_ids = parking.get_vehicle_by_age(ip[1])
            print(' '.join(registration_ids))
        
        elif ip[0] == 'Slot_number_for_car_with_number':
            slot = parking.get_slot(ip[1])
            print(slot)


__main__()