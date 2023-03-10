"""Restaurant rating lister."""
from random import choice

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
        res_score = int(input("Enter score: "))

        if res_score > 5 and res_score < 1:
            print("Please enter a score between 1 and 5.")
            continue

        ratings[res_name] = res_score
        add_resturant = input("Do you want to add a resturant. Y/N: ")

#Allow user to update random rating



#Sorting dictionary
    sorted_rating = sorted(ratings)

#print dictionary 
    for show in sorted_rating:
        print (f"{show} is rated a {ratings[show]}. ")
    


if __name__ == '__main__':    
    resturant_ratings("scores.txt")
