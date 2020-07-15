"""Generate int type input data"""


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module speedsurprises.numbers.factorial --function compute_iterative_factorial --types custom --data_directory ../Tada-Generate-Functions/ --data_module generatefunctions.generate_numbers --data_function generate_single_int --startsize 25 --maxsize 100 --log
def generate_single_int(chosen_size):
    """Generate an int value"""
    return (int(chosen_size),)


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module speedsurprises.graph.graph_gen --function graph_gen --types custom --data_directory ../Tada-Generate-Functions/ --data_module generatefunctions.generate_numbers --data_function generate_double_int --startsize 25 --maxsize 100 --log
def generate_double_int(chosen_size):
    """Generate an int value"""
    return (int(chosen_size), int(chosen_size))


def generate_double_int_first_position(chosen_size):
    """Generate an int value"""
    return (int(chosen_size), 0)


def generate_double_int_second_position(chosen_size):
    """Generate an int value"""
    return (0, int(chosen_size))


def generate_bitdepth(chosen_size):
    """Generate an int value"""
    lowerbound = 10 ** (int(chosen_size) - 1)
    upperbound = (10 ** int(chosen_size)) - 1
    return random.randint(lowerbound, upperbound)
