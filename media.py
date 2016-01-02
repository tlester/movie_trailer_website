''' This module created by Tom Lester for the Full Stack Nano Degree.'''
import webbrowser

class Movie(object):
    ''' Movie class creates a data structure for movie information.

        The Movie class takes in four arguments:
        movie_tite:  The Title of the movie.
        movie_storyline:  A synopsis of the movie.
        poster_image:  A link to the movie's poster.
        trailer_youtube:  The url of the trailer on youtube.
    '''

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        ''' This method opens the youtube trailer. '''
        webbrowser.open(self.trailer_youtube_url)
