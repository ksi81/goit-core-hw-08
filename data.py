import pickle

# Десеріалізація об'єкта з файлу
with open('addres_book', 'rb') as file:
    deserialized_data = pickle.load(file)

# Виведе вихідний об'єкт Python
print(deserialized_data)