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
		self.numRecommendation = 10

		self.classification = 0
		self.construction = 1

		self.init()

	def init(self):
		with open("movie_metadata.csv", 'rb') as f:
			self.movies = list(csv.reader(f, delimiter=','))

		for i in range(len(self.movies)-1):
			self.moviesName.append(str(self.movies[i+1][11]).strip()[:-2].decode("utf8"))

	def getFavoriteActors(self):
		self.favoriteActors.clear()
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
		self.favoriteDirectors.clear()
		numFavoriteMovies = len(self.favoriteMovies)
		for i in range(numFavoriteMovies):
			movieIdx = self.favoriteMovies[i]
			director = self.movies[movieIdx][self.directorIdx]
			if self.favoriteDirectors.has_key(director):
				self.favoriteDirectors[director] += 1
			else:
				self.favoriteDirectors[director] = 1

	def getFavoriteGenres(self):
		self.favoriteGenres.clear()
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

	def getMovieRecommendationNames(self, favoriteMovies, kbsType):
		self.favoriteMovies = favoriteMovies
		self.getFavoriteActors()
		self.getFavoriteDirectors()
		self.getFavoriteGenres()
		movieScores = []
		for i in range(len(self.movies)):
			movieScores.append(self.countWeight(i))
		arr = np.array(movieScores)
		numFavoriteMovies = len(favoriteMovies)
		recommendedMovies =  arr.argsort()[-(numFavoriteMovies+self.numRecommendation):][::-1]
		deletedIdx = []
		for i in range(len(recommendedMovies)):
			if recommendedMovies[i] in self.favoriteMovies:
				deletedIdx.append(i)		
		recommendedMovies = np.delete(recommendedMovies,deletedIdx)
		if kbsType == self.classification:
			recommendedMovies = recommendedMovies[:1]
		elif kbsType == self.construction:
			recommendedMovies = recommendedMovies[:self.numRecommendation]
		else:
			recommendedMovies = recommendedMovies[:0]
		recommendedMoviesName = []
		for idx in recommendedMovies:
			recommendedMoviesName.append(str(self.movies[idx][11]).strip()[:-2].decode("utf8"))
		return recommendedMoviesName

	def getMoviesName(self):
		return self.moviesName

def main():
	movie = Movie()

if __name__ == "__main__":
    main()