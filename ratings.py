"""Restaurant rating lister."""


def resturant_ratings(filename):
    with open(filename, "r") as reader:
        ratings = {}

        for line in reader:
            line = line.rstrip().split(":")
            ratings[line[0]] = line[1]

        sorted_rating = sorted(ratings)

        for show in sorted_rating:
            print (f"{show} is rated a {ratings[show]}. ")


if __name__ == '__main__':    
    resturant_ratings("scores.txt")
