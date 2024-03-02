import json

def write_contacts_to_file(filename, contacts):
    data = {"contacts": contacts}
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

def read_contacts_from_file(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        contacts = data.get("contacts", [])
    return contacts

# Приклад використання:
some_data = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

write_contacts_to_file("contacts.json", [some_data])
contacts = read_contacts_from_file("contacts.json")
print(contacts)
