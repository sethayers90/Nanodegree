import webbrowser
'''
Importing webbrowser to make it so I can use YouTube
to be able to see the movie trailer.
Also, creating class Movie to be able to
store the same values for multiple movies.
'''


class Movie():
    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
