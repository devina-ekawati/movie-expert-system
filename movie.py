import re, string
import csv

movies = []
favoriteActors = {}
favoriteDirectors = {}
favoriteMovies = [1,2,3,4,19,27,34]

actorIdx = [10, 6, 14]
directorIdx = 1

def init():
	with open("movie_metadata.csv", 'rb') as f:
		global movies
		movies = list(csv.reader(f, delimiter=','))

def getFavoriteActors():
	numFavoriteMovies = len(favoriteMovies)
	for i in range(numFavoriteMovies):
		movieIdx = favoriteMovies[i]
		numActors = len(actorIdx)
		for j in range(numActors):
			actor = movies[movieIdx][actorIdx[j]]
			if favoriteActors.has_key(actor):
				favoriteActors[actor] += 1
			else:
				favoriteActors[actor] = 1

def getFavoriteDirectors():
	numFavoriteMovies = len(favoriteMovies)
	for i in range(numFavoriteMovies):
		movieIdx = favoriteMovies[i]
		director = movies[movieIdx][directorIdx]
		if favoriteDirectors.has_key(director):
			favoriteDirectors[director] += 1
		else:
			favoriteDirectors[director] = 1

def countWeight(movieIdx):
	pass

def main():
	init()
	print len(movies)
	getFavoriteActors()
	print favoriteActors
	getFavoriteDirectors()
	print favoriteDirectors

if __name__ == "__main__":
    main()