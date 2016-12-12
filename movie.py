import re, string
import csv



def main():
	with open("movie_metadata.csv", 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			print row[10]
	


if __name__ == "__main__":
    main()