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
	actors = countActors()
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

		for j in range(numActors):
			actor = movies[movieIdx][actorIdx[j]]
			# print actor, actors[actor]
			if actors[actor] < 3:
				del favoriteActors[actor]

def countActors():
	actors = {}
	numMovies = len(movies) - 1
	for i in range(numMovies):
		numActors = len(actorIdx)
		for j in range(numActors):
			actor = movies[i+1][actorIdx[j]]
			if actors.has_key(actor):
				actors[actor] += 1
			else:
				actors[actor] = 1
	return actors

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
	getFavoriteActors()
	print favoriteActors
	getFavoriteDirectors()
	print favoriteDirectors

if __name__ == "__main__":
    main()