from flask import Flask, request, session, redirect, url_for, render_template
from movie import Movie

app = Flask(__name__)
movie = Movie()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', search=True, moviesList=movie.getMoviesName())
    else:
        return get_result()

def get_result():
	selected = request.form.getlist('keyword', None)
	favoriteMovies = []
	for val in selected:
		favoriteMovies.append(int(val))
	return render_template('index.html',moviesList=movie.getMoviesName(), movies=movie.getMovieRecommendationNames(favoriteMovies))

if __name__ == '__main__':
    app.run()