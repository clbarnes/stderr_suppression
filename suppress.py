import re
import sys


class NullErr():
    REGEX = r"({})|(^\s$)"

    def __init__(self, regex_str=r"(?s).*"):
        self.stderr = sys.stderr
        self.regex = re.compile(NullErr.REGEX.format(regex_str))

    def write(self, s):
        if self.regex.match(s):
            pass
        else:
            self.stderr.write(s)


class WarningSuppressor():
    def __init__(self, regex_str):
        self.null_err = NullErr(regex_str)
        self.std_err = sys.stderr

    def __enter__(self):
        sys.stderr = self.null_err
        return self

    def __exit__(self, *args):
        sys.stderr = self.std_err
