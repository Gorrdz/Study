from pathlib import Path
import os, shutil, sys
from os.path import split

dir_path = Path(sys.argv[1])

folders_and_types = {
    'images' : ['.jpg', '.png', '.jpeg', 'svg'],
    'videos' : ['.avi', '.mp4', '.mov', '.mkv'],
    'documents' : ['.doc', '.docx', '.txt', '.pdf', '.xls', '.pptx'],
    'audio' : ['.mp3', '.ogg', '.wav', '.amr'],
    'archives' : ['.zip', '.gz', '.tar']}

def create_folders(path, folder):
    for folder in folders_and_types:
        if not os.path.exists(f'{path}\\{folder}'):
            os.mkdir(f'{path}\\{folder}')

def normalize(item_path):
    CYRILLIC_SYMBOLS = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
                    "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "є", "і","ї","ґ", " ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-","+","=")
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t",
                   "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_","_","_","_")
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
        table = item_path.maketrans(TRANS)
    return str(item_path).translate(table)

def sort_files():
    
    create_folders(dir_path,folders_and_types)
        
    for item in dir_path.glob('**/*'):
        
        if item.is_file() and item.suffix.lower() in folders_and_types['images']:
            destination = os.path.join(dir_path, 'images', item.name)
            if item == Path(destination):
                continue
            try:
                os.rename(item, normalize(destination))
            except FileExistsError:
                continue

        if item.is_file() and item.suffix.lower() in folders_and_types['videos']:
            destination = os.path.join(dir_path, 'videos', item.name )
            if item == Path(destination):
                continue
            try:
                os.rename(item, normalize(destination))
            except FileExistsError:
                continue

        if item.is_file() and item.suffix.lower() in folders_and_types['documents']:
            destination = os.path.join(dir_path, 'documents', item.name )
            if item == Path(destination):
                continue
            try:
                os.rename(item, normalize(destination))
            except FileExistsError:
                continue
            
        if item.is_file() and item.suffix.lower() in folders_and_types['audio']:
            destination = os.path.join(dir_path, 'audio', item.name )
            if item == Path(destination):
                continue
            try:
                os.rename(item, normalize(destination))
            except FileExistsError:
                continue

        if item.is_file() and item.suffix.lower() in folders_and_types['archives']:
            destination = os.path.join(dir_path, 'archives', item.stem)
            if item == Path(destination):
                continue
            shutil.unpack_archive(item, destination)
           
            
        else:
             continue

    for item in dir_path.glob('**/*'):
        if item.is_dir() and not len(os.listdir(item)):
            os.rmdir(item)

    print ('Everything is done!') 


sort_files() 







       




