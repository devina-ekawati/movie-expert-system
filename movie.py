import re, string
import csv

movies = []

def init():
	with open("movie_metadata.csv", 'rb') as f:
		movies = csv.reader(f, delimiter=',')

def main():
	init()
	


if __name__ == "__main__":
    main()