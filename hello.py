#!/usr/bin/env python

# Zen of Python
# import this

import logging
import math
import random
import sys
import webbrowser
from math import sin
from typing import Optional


def count_lines(file_name: str) -> Optional[int]:
    """
    Count the number of lines in a file.
    If the file can't be opened, it should
    be almost treated the same as if it was empty.
    """
    try:
        return len(open(file_name, "r").readlines())
    except EnvironmentError:
        return None


def count_lines_1(filename):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        return len(open(filename, "r").readlines())
    except:  # noqa: E722
        print("exception error reading the file or calculating lines!")
        # Something went wrong reading the file or calculating the number of lines.
        return 0


myfile = input("Enter a file to open:  ")
print(count_lines(myfile))


def count_lines_2(file_name):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        return len(open(file_name, "r").readlines())
    except IOError:
        # Something went wrong reading the file.
        return 0


my_file = input("Enter a file to open:  ")
print(count_lines(my_file))


def count_lines_3(file_name):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        return len(open(file_name, "r").readlines())
    except EnvironmentError:
        # Something went wrong reading the file.
        return 0


def count_lines_4(file_name):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        return len(open(file_name, "r").readlines())
    except (EnvironmentError, TypeError):
        # Something went wrong reading the file.
        return 0


def count_lines_5(file_name):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        return len(open(file_name, "r").readlines())
    except (EnvironmentError, TypeError) as e:
        # Something went wrong reading the file.
        logging.error(e)
        return 0


def count_lines_6(file_name):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        return len(open(file_name, "r").readlines())
    except TypeError as e:
        # The filename wasn't valid for use with the filesystem.
        logging.error(e)
        return 0
    except EnvironmentError as e:
        # Something went wrong reading the file.
        logging.error(e.args[1])
        return 0


def get_value(dictionary, name):
    try:
        return dictionary[name]
    except Exception as e:
        print("exception hit..writing to file")
        log = open("logfile.txt", "w")
        log.write("%s\n" % e)
        log.close()


names = {"Jack": 113, "Jill": 32, "Yoda": 395}
print(get_value(names, "Jackz"))  # change to Jack and it runs fine


def validate_5(value, validator):
    try:
        return validator(value)
    except Exception as e:
        raise ValueError("Invalid value: %s" % value) from e


def validator(value):
    if len(value) > 10:
        raise ValueError("Value can't exceed 10 characters")


validate_5("test", validator)
# validate_5(False, validator)


def main() -> None:
    print("Hello from pro-python-3!")
    print(f"sin: {sin(math.pi / 4)}")
    print(f"sin: {sin(math.pi / 2)}")


def checker(x: int, y: int) -> int:
    if x > 0 and y > 100:
        raise ValueError("Value for y is too large.")
    elif x > 0:
        return y
    elif x == 0:
        return False
    else:
        raise ValueError("Value for x cannot be negative.")


def checker_alt(x: int, y: int) -> bool | int:
    match x, y:
        case 0, _:
            return False
        case x, y if x > 0 and y > 100:
            raise ValueError("Value for y is too large.")
        case x, y if x > 0:
            return y
        case _:
            raise ValueError("Value for x cannot be negative.")


def validate(data) -> None:
    if data["username"].startswith("_"):
        raise ValueError("Username must not begin with an underscore.")


def validate_1(data: dict) -> None:
    if "username" in data and data["username"].startswith("_"):
        raise ValueError("Username must not begin with an underscore.")


def validate_2(data: dict) -> None:
    if "username" in data and data["username"].startswith("_"):
        raise ValueError("Username must not begin with an underscore.")


def count_lines_7(file_name):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        file = open(file_name, "r")
    except TypeError as e:
        # The filename wasn't valid for use with the filesystem.
        logging.error(e)
        return 0
    except EnvironmentError as e:
        # Something went wrong reading the file.
        logging.error(e.args[1])
        return 0
    return len(file.readlines())


def count_lines_8(filename):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        file = open(filename, "r")
    except TypeError as e:
        # The filename wasn't valid for use with the filesystem.
        logging.error(e)
        return 0
    except EnvironmentError as e:
        # Something went wrong reading the file.
        logging.error(e.args[1])
        return 0
    else:
        return len(file.readlines())


def count_lines_9(file_name):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    file = None  # file must always have a value
    try:
        file = open(file_name, "r")
        lines = file.readlines()
    except TypeError as e:
        # The filename wasn't valid for use with the filesystem.
        logging.error(e)
        return 0
    except EnvironmentError as e:
        # Something went wrong reading the file.
        logging.error(e.args[1])
        return 0
    except UnicodeDecodeError as e:
        # The contents of the file were in an unknown encoding.
        logging.error(e)
        return 0
    else:
        return len(lines)
    finally:
        if file:
            file.close()


def echo():
    """Returns everything you type until you press Ctrl-C"""
    while True:
        try:
            print(input("Type Something or CTRL C to exit: "))
        except KeyboardInterrupt:
            print()  # Make sure the prompt appears on a new line.
            print("bye for now...:")
            break


echo()


def count_lines_10(file_name):
    """Count the number of lines in a file."""
    file = open(file_name, "r")
    try:
        return len(file.readlines())
    finally:
        file.close()


# count_lines_10("fu")


def count_lines_11(file_name):
    """Count the number of lines in a file."""
    with open(file_name) as file:
        return len(file.readlines())


def test_value(value):
    if value < 100:
        return "The value is just right."
    else:
        return "The value is too big!"


print(test_value(55))


def test_value_1(value):
    return "The value is " + ("just right." if value < 100 else "too big!")


print(test_value_1(55))

if __name__ == "__main__":
    main()

    n = random.randint(0, 1)
    count: Optional[int] = None
    match n:
        case 0 | 1:
            count = count_lines("hello.py")
        case _:
            count = count_lines("pyproject.toml")
    match count:
        case None:
            print("Couldn't open file.")
        case n:
            print(f"number of lines: {count}")

    username = sys.argv[1]
    try:
        validate_2({"username": username})
    except (TypeError, ValueError) as e:
        print(e)
        # out of range since username is empty and there is no
        # second [1] position
    last_name = "Smith"
    count = 0
    for letter in last_name:
        print(f"{letter} {count}")
        count += 1
    print("---and the second loop----")
    count = 0
    while count < 5:
        print(f"{last_name[count]} {count}")
        count += 1
    webbrowser.open_new("http://www.python.org/")
    # more info at:  https://docs.python.org/3.4/library/webbrowser.html
    for x in range(5):
        print(x)
    rr = range(5)
    rr = range(0, 5)
    lst = list(range(5))
