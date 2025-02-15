import pickle

def create():
    with open('librarydetails.txt', 'wb') as k1:
        while True:
            data = {}
            data['bookname'] = input('Enter the book name: ')
            data['bookno'] = input('Enter the book no.: ')
            data['author'] = input('Enter the author name: ')
            data['price'] = 1000
            pickle.dump(data, k1)
            choice = input('Press Y/y to continue: ')
            if choice not in 'Yy':
                break

def access():
    with open('librarydetails.txt', 'rb') as k1:
        try:
            while True:
                d = pickle.load(k1)
                print('*' * 50)
                print('\t\t Book Details')
                print('*' * 50)
                print('\n Book Name   :', d['bookname'])
                print('\n Book Number :', d['bookno'])
                print('\n Author      :', d['author'])
                print('\n Price       :', d['price'])
                print('\n')
        except EOFError:
            print('End Of All Records')
            input('Press anything to continue')

def search(bno):
    with open('librarydetails.txt', 'rb') as k1:
        h = 0
        try:
            while True:
                d = pickle.load(k1)
                if d['bookno'] == bno:
                    print('*' * 50)
                    print('\t\t Book Details')
                    print('*' * 50)
                    print('\n Book Name   :', d['bookname'])
                    print('\n Book Number :', d['bookno'])
                    print('\n Author      :', d['author'])
                    print('\n Price       :', d['price'])
                    print('\n')
                    h = 1
                    break
        except EOFError:
            if h == 0:
                print('NO DATA FOUND')
            else:
                print('RECORD FOUND')
            input('Press anything to continue')

while True:
    print('1 - Creation')
    print('2 - Accessing')
    print('3 - Searching')
    print('4 - Exit')
    j = int(input('Enter your choice: '))
    
    if j == 1:
        create()
    elif j == 2:
        access()
    elif j == 3:
        m = input('Enter the book number: ')
        search(m)
    elif j == 4:
        print('End of the project. Thank You!!')
        break
    else:
        print('Invalid choice, please try again')
