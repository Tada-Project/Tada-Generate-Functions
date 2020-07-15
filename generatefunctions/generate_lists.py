"""Generate list type input data"""

import random


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module speedsurprises.lists.python_basic --function list_copy --types custom --data_directory ../Tada-Generate-Functions/ --data_module generatefunctions.generate_lists  --data_function generate_single_int_list --startsize 25 --maxsize 100 --log
def generate_single_int_list(chosen_size):
    """Generate an int list"""
    output = [random.random() for _ in range(int(chosen_size))]
    return (output,)


def generate_double_int_list(chosen_size):
    """Generate an int list"""
    output = [random.random() for _ in range(int(chosen_size))]
    output2 = [random.random() for _ in range(int(chosen_size))]
    return (output, output2)


def generate_single_char_list(chosen_size):
    """Generate a char list"""
    output = [
        random.choice(string.ascii_letters + string.digits)
        for _ in range(int(chosen_size))
    ]
    return (output,)


def generate_double_char_list(chosen_size):
    """Generate a char list"""
    output = [
        random.choice(string.ascii_letters + string.digits)
        for _ in range(int(chosen_size))
    ]
    output2 = [
        random.choice(string.ascii_letters + string.digits)
        for _ in range(int(chosen_size))
    ]
    return (output, output2)
