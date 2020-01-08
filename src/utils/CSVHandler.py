import pandas


def read_csv(filename):
    dataframe = pandas.read_csv(filename)
    return dataframe


def write_csv(filename,content):
    with open(filename) as f:
        f.write(content)
    f.close()