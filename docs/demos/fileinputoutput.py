"""File Input Output example"""

handle = None

try:

    handle = open('nomefile.txt', 'w')

    # Esemplificativo di altre istruzioni che possono generare una eccezione.
    input("Press Enter to continue...")

except FileNotFoundError:

    print('File non trovato!')

except OSError:

    # Re-raise exception?
    print('Errore generico!')

finally:

    print('In finally...')

    if handle:

        print('Closing...')

        try:

            # Can throw IOError if quota is reached when flushing...
            handle.close()

        except IOError:

            print('Error when closing...')
