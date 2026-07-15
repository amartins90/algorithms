import csv
import collections
import string


def read_data(filename):
    with open(filename) as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        next(reader, None)  # skip the headers
        data = [row for row in reader]
    return data

def tokenizer(data):
    tokens = {}
    translator = str.maketrans("", "", string.punctuation)

    for item in data:
        movie_id = item[0]
        overview = item[2].lower().translate(translator).split(" ")
        tokens[movie_id] = dict(collections.Counter(overview))

    return tokens

def tf_calculator():
    return


filename = "data/movies_overview.csv"
data = read_data(filename)
tokens = tokenizer(data)
print(tokens)