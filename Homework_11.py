from collections import UserDict
from datetime import date, datetime
import re

class AddresBook(UserDict):
    def add_record(self, record):
        database.data[record.name.value] = [record.phone.value]
   
    def iterator(self):
        self.my_dict = list(database.data)
        index = 0
        while index < len(self.my_dict):
            print (self.my_dict[index])
            index += 1
            if (index % 5) == 0:
                input('---------------')
        else:
            StopIteration  

class Field:
   def __init__(self, value):
        self.value = value
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if str(new_value).isdigit():
            self.__value = new_value
        else:
            print ('Phone number should contain digits only')
            raise ValueError

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        pattern = r'\d{4}-\d{2}-\d{2}'
        if re.match(pattern, new_value):
            self.__value = new_value
        else:
            print ('Birthday date should be YYYY-MM-DD')
            raise ValueError

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def add_phone(self):
        database.data[self.name.value].append(self.phone.value)
        
    def del_phone(self):
        for key, value in database.data.items():
            if self.name.value in key and self.phone.value in value:
                value.pop(value.index(self.phone.value))

    def del_phone_all(self):
        database.data[self.name.value] = []

    def days_to_birthday(self):
        real_date = datetime.strptime(self.birthday.value, '%Y-%m-%d').date()
        if real_date.month > date.today().month:
            next_birthday = real_date.replace(datetime.now().year)
        elif real_date.month < date.today().month:
            next_birthday = real_date.replace(datetime.now().year + 1)
        days_to_birthday = next_birthday - date.today()
        return f'{days_to_birthday.days} days until next Birthday'
         
database = AddresBook()
 
def hello():
    return 'How can I help you?'

def input_error(func):
    def inner():
        try:
            result = func()
        except IndexError:
            return print ('IndexError. It looks like you missed something')
        except ValueError:
            return print ('ValueError. You have entered wrong data')
        except KeyError:
            return print ('KeyError. Command you have entered is not exist')
        else:
            return result
    return inner

@input_error
def main():
    end_list = ['good bye', 'close', 'exit']
    string = input(':')
    if string in end_list:
        return string
    
    split = string.split()
    
    if len(split) == 4:
        record = Record(Name(split[1]), Phone(split[2]), Birthday(split[3]))
    elif len(split) == 3:
        record = Record(Name(split[1]), Phone(split[2]))
    
    command = split[0].lower()
    
    if command == 'hello':
        return print(hello())
    
    elif command == 'add':
        if record.name.value in database.data:
            record.add_phone()
            if record.birthday:
                return print(f'Another phone number for user {record.name.value} has added and {record.days_to_birthday()} left')
            elif not record.birthday:
                return print(f'Another phone number for user {record.name.value} has added')
        else:
            database.add_record(record)
            if record.birthday:
                return print(f'New entry {record.name.value} has added and {record.days_to_birthday()} left')
            elif not record.birthday:
                return print(f'New entry {record.name.value} has added')

    elif command == 'del_phone':
        if record.phone.value == 'all':
            record.del_phone_all()
            return print('All phone numbers were deleted')
        else:
            record.del_phone()
            return print('Number deleted')
    
    elif command == 'phone':
        if split[1] in database.data:
            return print(f'Phone number(s) of {split[1]} is(are) {database.data[split[1]]}')
    
    elif command == 'change':
        if record.name.value in database.data:
            record.del_phone_all()
            record.add_phone()
    
    elif string.lower() == 'show all':
        return database.iterator()
        
while True:
    end_list = ['good bye', 'close', 'exit']
    if main() in end_list:
        print ('Session is over')
        break
    else:
        main()

        
        
        
