"""File Input Output example using with statement"""

try:
    with open('nomefile.txt', 'w') as file:
        print('In with statement...')

    print('Fuori da with...')

except OSError:
    print('Errore generico!')
