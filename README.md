# Tada-Generate-Functions
A Python 3 Package with Data Generation Functions for Tada, the tool for auTomAtic orDer of growth Analysis


## Running Experiment with Tada-Generate-Functions

This repository provides data generation functions for tada, and can be used with speed-surprises to do some sample experiments and analysis.

We recommend you to download these three repositories with the  like this:

```
folder/
│
├── tada/
├── speed-surprises/
└── tada-generate-functions/
```

With the above setting, you can navigate to tada's main directory and run the following sample command:

```bash
pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.lists.python_basic --function list_copy --types custom --data_directory ../Tada-Generate-Functions/ --data_module generatefunctions.generate_lists  --data_function generate_single_int_list --startsize 25 --maxsize 1000
```

## Adding New Functions to the Tada-Generate-Functions

Following are two sample data generation functions that can be used for tada:

```python
def generate_single_int(chosen_size):
    """Generate an int value"""
    return (int(chosen_size),)


def generate_double_int(chosen_size):
    """Generate an int value"""
    return (int(chosen_size), int(chosen_size))

```

#### Function Input

The data generation functions suppose to take an integer (the size of the problem of the current round of experiment) as the input, this input integer will keep doubling through out the experiment.

#### Function Output

Functions output suppose to return the data you want to pass into the analyzed function. If the analyzed function takes only one argument, the data must be surrounded as `(<generated data>, )` to make the generation function output an iterable data.

If the analyzed function takes multiple arguments, the return statement can be `(<generated data>, <second generated data>)` or `(<generated data>, <second generated data>, <third generated data>)`.
