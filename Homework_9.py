database = {}

def hello():
    return 'How can I help you?'
def add_contact(name, phone):
    database[name] = phone
    return 'New entry was added'
def show_phone_number(name):
    if name in database:
        return f'{name}\'s phone number is {database[name]}'
def change_phone_number(name, phone):
    if name in database:
        database[name] = phone
        return f'Phone number of {name} was succesfully changed'
def show_all():
    return database

KEY_WORDS = {
             'add' : add_contact,
             'change' : change_phone_number,
            }
KEY_WORDS_SERVICE = {'hello' : hello,
                     'show all' : show_all,
                     'phone' : show_phone_number}

def handler(key_word):
    return KEY_WORDS[key_word]

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
    if split[0].lower() in KEY_WORDS:
        return print(KEY_WORDS[split[0].lower()](split[1], split[2]))
    elif split[0].lower() == 'hello':
        return print(KEY_WORDS_SERVICE[split[0].lower()]())
    elif split[0].lower() == 'phone':
        return print(KEY_WORDS_SERVICE[split[0].lower()](split[1]))
    elif string.lower() == 'show all':
        return print(KEY_WORDS_SERVICE[string.lower()]())

while True:
    end_list = ['good bye', 'close', 'exit']
    if main() in end_list:
        print ('Session is over')
        break
    else:
        main()

        
        
        
