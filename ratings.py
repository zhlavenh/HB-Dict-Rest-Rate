"""Restaurant rating lister."""


def resturant_ratings(filename):
    ratings = {}

# Reading file and storing it in dictionary
    with open(filename, "r") as reader:

        for line in reader:
            line = line.rstrip().split(":")
            ratings[line[0]] = line[1]

#Asking user for prompt and adding input to dictionary
    add_resturant = input("Info from file retrieved.\nDo you want to add a resturant. Y/N: ")

    while add_resturant == "Y" or add_resturant == "y":
        res_name = input("Enter resturant name: ")
        res_score = input("Enter score: ")
        ratings[res_name] = res_score
        add_resturant = input("Do you want to add a resturant. Y/N: ")

#Sorting dictionary
    sorted_rating = sorted(ratings)

#print dictionary 
    for show in sorted_rating:
        print (f"{show} is rated a {ratings[show]}. ")
    


if __name__ == '__main__':    
    resturant_ratings("scores.txt")
