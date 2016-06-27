"""
contains helper methods
"""


def convertToFloat(seq):
    """
    convert items in seq to float type
    """
    seq = [float(item) for item in seq]
    return seq
