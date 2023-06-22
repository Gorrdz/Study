from collections import UserDict

class AddresBook(UserDict):
    def add_record(self, record):
        database.data[record.name.value] = [record.phone.value]

class Field:
   def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def add_phone(self):
        database.data[self.name.value].append(self.phone.value)
        
    def del_phone(self):
        for key, value in database.data.items():
            if self.name.value in key and self.phone.value in value:
                value.pop(value.index(self.phone.value))

    def del_phone_all(self):
        database.data[self.name.value] = []
    
            
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
    command = split[0].lower()
    
    if command == 'hello':
        return print(hello())
    
    elif command == 'add':
        record = Record(Name(split[1]), Phone(split[2]))
        if record.name.value in database.data:
            record.add_phone()
            return print('Another phone number has added')
        else:
            database.add_record(record)
            return print('New entry has added')
        
    elif command == 'del_phone':
        record = Record(Name(split[1]), Phone(split[2]))
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
        record = Record(Name(split[1]), Phone(split[2]))
        if record.name.value in database.data:
            record.del_phone_all()
            record.add_phone()
        

    elif string.lower() == 'show all':
        for k, v in database.data.items():
            print (f'{k} - {v}')


while True:
    end_list = ['good bye', 'close', 'exit']
    if main() in end_list:
        print ('Session is over')
        break
    else:
        main()

        
        
        
