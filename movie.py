import re, string
import csv

class Movie:
	def __init__(self):
		self.movies = []
		self.favoriteActors = {}
		self.favoriteDirectors = {}
		self.favoriteGenres = {}
		self.favoriteMovies = [1,2,3,4,19,27,34]

		self.actorIdx = [10, 6, 14]
		self.directorIdx = 1
		self.genreIdx = 9

	def init(self):
		with open("movie_metadata.csv", 'rb') as f:
			self.movies = list(csv.reader(f, delimiter=','))

	def getFavoriteActors(self):
		actors = self.countActors()
		numFavoriteMovies = len(self.favoriteMovies)
		for i in range(numFavoriteMovies):
			movieIdx = self.favoriteMovies[i]
			numActors = len(self.actorIdx)
			for j in range(numActors):
				actor = self.movies[movieIdx][self.actorIdx[j]]
				if self.favoriteActors.has_key(actor):
					self.favoriteActors[actor] += 1
				else:
					self.favoriteActors[actor] = 1

			for j in range(numActors):
				actor = self.movies[movieIdx][self.actorIdx[j]]
				# print actor, actors[actor]
				if actors[actor] < 3:
					del self.favoriteActors[actor]

	def countActors(self):
		actors = {}
		numMovies = len(self.movies) - 1
		for i in range(numMovies):
			numActors = len(self.actorIdx)
			for j in range(numActors):
				actor = self.movies[i+1][self.actorIdx[j]]
				if actors.has_key(actor):
					actors[actor] += 1
				else:
					actors[actor] = 1
		return actors

	def getFavoriteDirectors(self):
		numFavoriteMovies = len(self.favoriteMovies)
		for i in range(numFavoriteMovies):
			movieIdx = self.favoriteMovies[i]
			director = self.movies[movieIdx][self.directorIdx]
			if self.favoriteDirectors.has_key(director):
				self.favoriteDirectors[director] += 1
			else:
				self.favoriteDirectors[director] = 1

	def getFavoriteGenres(self):
		numFavoriteMovies = len(self.favoriteMovies)
		for i in range(numFavoriteMovies):
			movieIdx = self.favoriteMovies[i]
			genres = self.movies[movieIdx][self.genreIdx].split("|")
			numGenres = len(genres)
			for j in range(numGenres):
				genre = genres[j]
				if self.favoriteGenres.has_key(genre):
					self.favoriteGenres[genre] += 1
				else:
					self.favoriteGenres[genre] = 1

	def countWeight(movieIdx):
		pass

def main():
	movie = Movie()
	movie.init()
	movie.getFavoriteActors()
	print movie.favoriteActors
	movie.getFavoriteDirectors()
	print movie.favoriteDirectors
	movie.getFavoriteGenres()
	print movie.favoriteGenres

if __name__ == "__main__":
    main()