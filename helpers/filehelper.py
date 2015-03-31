__author__ = 'Jason Poh'


def write_to_file(contents, file_path):
    try:
        f = open(file_path, "w+")
        f.write(contents)
        f.close()
    except IOError:
        return False
    return True


def append_to_file(contents, file_path):
    try:
        f = open(file_path, "a")
        f.write(contents)
        f.close()
    except IOError:
        return False
    return True


def read_lines(file_path):
    try:
        f = open(file_path)
        lines = f.readlines()
        f.close()
    except IOError:
        return False
    return lines

def get_injection_points_file():
    f = open("data/seeds.json", "w+")
    return f

