def funzione_senza_argomenti():
    print('Questa è una funzione senza argomenti')


def funzione_con_argomenti_posizionali(arg1, arg2, arg3):
    print('Questa è una funzione con argomenti posizionali')


def funzione_che_ritorna_un_valore():
    print('Questa è una funzione che ritorna il valore True')
    return True


def funzione_con_argomenti_di_default(arg1, arg2, arg3='default', arg4='default'):
    print('Arg1: {}'.format(arg1))
    print('Arg2: {}'.format(arg2))
    print('Arg3: {}'.format(arg3))
    print('Arg4: {}'.format(arg4))

def funzione_con_argomenti_variabili(arg1, arg2, *arguments, **kwargs):
    print('Arg1: {}'.format(arg1))
    print('Arg2: {}'.format(arg2))
    for arg in arguments:
        print(arg)
    for keyword in kwargs:
        print(keyword, ":", kwargs[keyword])
