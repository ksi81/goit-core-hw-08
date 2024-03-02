import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for contact in contacts:
            contact['favorite'] = str(contact['favorite']).lower()  # Переведення у строковий формат і приведення до нижнього регістру
            writer.writerow(contact)

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['favorite'] = row['favorite'].lower() == 'true'  # Переведення у логічне значення
            contacts.append(row)
    return contacts

