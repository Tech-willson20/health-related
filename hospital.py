dialysis_dict = {
    'Dialysis':880
}

Appointment = []

def book_appointment(name, service, discount_code = None):
    if service not in dialysis_dict:
        return 'Service not available'
    
    total_cost = dialysis_dict[service]
    if discount_code == 'pyclubs':
        total_cost *= 0.3
        Appointment.append({'name': name, 'service': service, 'total_cost': total_cost})
        return f'Appointment booked for {name}. Total cost is GHC {total_cost} '

def display_appointment():
    if not Appointment:
        return 'No appointment booked'
    else:
        return Appointment
    
print(book_appointment('John', 'Dialysis', 'pyclubs'))
print(book_appointment('Alice', 'Physiotherapy'))
print(display_appointment())

    #Appointment_list = 'Appointment booked\n'
    #for i, (name, service, discount_code) in enumerate(Appointment, start = 1):
    #    return Appointment_list += f"{i}. Patient name: {name}, Service: {service}, Total price: {total_cost} "
    #return Appointment_list

