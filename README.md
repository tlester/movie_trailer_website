# Movie Trailer Website
This is a python application that builds a website of my favorite movies.  

## Install
To install from git, run the following command:
```
git clone https://github.com/tlester/movie_trailer_website.git
```
Or you can download the zip from [here](https://github.com/tlester/movie_trailer_website/archive/master.zip)

## Usage / Customizstion

You can run the applicaiton as is, but that would mean you would have a website
of MY favorite movies.  To make ths applicaiton more meaningful, I suggest that
you fill the website with YOUR favorite movies.  

To do this, edit the entertainment_center.py file.  Each movie looks like this:
```
VARIABLE_NAME = media.Movie('<movie_name>',
    '<movie description>',
    '<link to movie poster>',
    '<link to trailer on youtube>')
```
For example:
```
AVATAR = media.Movie('Avatar',
    'A paraplegic marine dispatched to the moon Pandora on a unique mission'
    ' becomes torn between following his orders and protecting the world'
    ' he feels is his home.',
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://youtu.be/5PSNL1qE6VY')
```
## Running the Application

To generate the web page, run the applicaton as follows:
```
$ python entertainment_center.py
```


