"""If statement template"""


def x_evaluation(value):
    """Demo function for if statement"""
    if value < 0:
        print('Less than zero!')
    elif value == 0:
        print('Zero!')
    elif value > 0:
        print('Greater than zero!')
    else:
        print('Never reached!')


x_evaluation(1)
