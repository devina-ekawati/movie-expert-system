import re, string
import csv
import numpy as np

class Movie:
	def __init__(self):
		self.movies = []
		self.moviesName = []
		self.favoriteActors = {}
		self.favoriteDirectors = {}
		self.favoriteGenres = {}
		self.favoriteMovies = []

		self.actorIdx = [10, 6, 14]
		self.directorIdx = 1
		self.genreIdx = 9

		self.actorScore = 3
		self.directorScore = 2
		self.genreScore = 4
		self.recommendedMovies = []
		self.recommendedMoviesName = []

		self.init()

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

	def countWeight(self, movieIdx):
		weight = 0
		movie = self.movies[movieIdx]
		numActors = len(self.actorIdx)
		for i in range(numActors):
			actor = movie[self.actorIdx[i]]
			if self.favoriteActors.has_key(actor):
				weight += self.favoriteActors[actor] * self.actorScore

		director = movie[self.directorIdx]
		if self.favoriteDirectors.has_key(director):
			weight += self.favoriteDirectors[director] * self.directorScore

		genres = movie[self.genreIdx].split("|")
		numGenres = len(genres)
		for i in range(numGenres):
			genre = genres[i]
			if self.favoriteGenres.has_key(genre):
				weight += self.favoriteGenres[genre] * self.genreScore

		return weight

	def getMovieRecommendationNames(self, favoriteMovies):
		self.favoriteMovies = favoriteMovies
		self.getFavoriteActors()
		self.getFavoriteDirectors()
		self.getFavoriteGenres()
		movieScores = []
		for i in range(len(self.movies)):
			movieScores.append(self.countWeight(i))
		arr = np.array(movieScores)
		self.recommendedMovies =  arr.argsort()[-20:][::-1]
		deletedIdx = []
		for i in range(len(self.recommendedMovies)):
			if self.recommendedMovies[i] in self.favoriteMovies:
				deletedIdx.append(i)		
		self.recommendedMovies = np.delete(self.recommendedMovies,deletedIdx)
		self.recommendedMovies = self.recommendedMovies[:10]
		for idx in self.recommendedMovies:
			self.recommendedMoviesName.append(str(self.movies[idx][11]).strip()[:-2])
		return self.recommendedMoviesName

	def getMoviesName(self):
		for i in range(len(self.movies)-1):
			self.moviesName.append(str(self.movies[i+1][11]).strip()[:-2])
		return self.moviesName

def main():
	movie = Movie()
	# print movie.getMovieRecommendationNames([1,2,3,4,19,27,34])
	# print movie.getMoviesName()

if __name__ == "__main__":
    main()