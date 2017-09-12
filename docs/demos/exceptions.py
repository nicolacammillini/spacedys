import sys, traceback

class MyExceptionHigher(Exception):
    pass

def inner_function_raising_lowerlevel_exception():
    try:
        open('nonexistentfile.txt')
    except IOError:
        print('Raising higher level exception...')
        raise MyExceptionHigher from IOError
    finally:
        print('In inner function finally')

def external_function():
    inner_function_raising_lowerlevel_exception()

try:
    external_function()
except MyExceptionHigher as myex:
    print('Higher level exception intercepted')
    #traceback.print_exc(file=sys.stdout)
