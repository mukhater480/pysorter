import os


def script_directory():
    """Returns the full path to where this script located"""
    return os.path.dirname(os.path.abspath(__file__))


def write_unknown(unknowns, path):
    """Appends all the unknown filetypes to the file at the given path.
    A filetype per line"""
    with open(path, 'a') as ufile:
        for i in unknowns:
            ufile.write(i)
            ufile.write('\n')
