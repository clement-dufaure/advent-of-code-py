import os

script_directory = os.path.dirname(os.path.abspath(__file__))


def get_input(name):
    return os.path.join(script_directory, "inputs", name)


def get_input_test(name):
    return os.path.join(script_directory, "inputs_test", name)
