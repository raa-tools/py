import sys

def getInput(prompt):
    """
    Function takes in prompt parameter as a string (eg. "File name:")
    Return user input function using 2 different methods (Py 3.X vs 2.X)
    """
    return input("{} ".format(prompt)) if sys.version_info[0] >= 3 else raw_input("{} ".format(prompt))
