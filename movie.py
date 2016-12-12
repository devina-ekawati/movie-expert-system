import re, string
import csv

movies = []
favoriteActors = {}
favoriteMovies = []

actorIdx = [10, 6, 14]

def init():
	with open("movie_metadata.csv", 'rb') as f:
		movies = csv.reader(f, delimiter=',')

def getFavoriteActors():
	numFavoriteMovies = len(favoriteMovies)
	for i in range(favoriteMovies):
		movieIdx = movies[i]
		numActors = len(actorIdx)
		for j in range(numActors):
			actor = movies[movieIdx[actorIdx[j]]]
			if favoriteActors.has_key(actor):
				favoriteActors[actor] += 1
			else:
				favoriteActors[actor] = 1

def countWeight(movieIdx):
	pass

def main():
	init()
	


if __name__ == "__main__":
    main()