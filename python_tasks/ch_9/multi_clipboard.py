
import pyperclip
import sys
import shelve

mcbShelf = shelve.open('mcb')


if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': 
    mcbShelf[sys.argv[2]] = pyperclip.paste() 
    print("done")


elif len(sys.argv) == 2: 
    
    
    if sys.argv[1].lower() == 'list': 
        pyperclip.copy(str(list(mcbShelf.keys()))) 
        print("listed")
    
    elif sys.argv[1] in mcbShelf: 
        pyperclip.copy(mcbShelf[sys.argv[1]])

    if sys.argv[1].lower() == 'delete':
        pyperclip.copy('')
        print('deleted')
mcbShelf.close()
