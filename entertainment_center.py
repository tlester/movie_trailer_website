''' This module acts as data structure for info about my favorite movies. '''
import media
import fresh_tomatoes

# Define properties for each movie we want to display.
KINGSMAN = media.Movie('Kingsman: Secret Service',
    'A spy organization recruits an unrefined, but promising street kid into'
    ' the agency\'s ultra-competitive training program, just as a global'
    ' threat emerges from a twisted tech genius.',
    'https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg', # NOQA
    'https://youtu.be/kl8F-8tR8to')

AVATAR = media.Movie('Avatar',
    'A paraplegic marine dispatched to the moon Pandora on a unique mission'
    ' becomes torn between following his orders and protecting the world'
    ' he feels is his home.',
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://youtu.be/5PSNL1qE6VY')

ST_INTO_DARKNESS = media.Movie('Star Trek Into Darkness',
    ' After the crew of the Enterprise find an unstoppable force of terror'
    ' from within their own organization, Captain Kirk leads a manhunt to'
    ' a war-zone world to capture a one-man weapon of mass destruction.',
    'https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg', # NOQA
    'https://youtu.be/QAEkuVgt6Aw')

GODFATHER = media.Movie('The Godfather',
    'The aging patriarch of an organized crime dynasty transfers control'
    ' of his clandestine empire to his reluctant son.',
    'https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
    'https://youtu.be/sY1S34973zA')

USUAL_SUSPECTS = media.Movie('The Usual Suspects',
    'A sole survivor tells of the twisty events leading up to a horrific gun'
    ' battle on a boat, which begin when five criminals meet at a'
    ' seemingly random police lineup.',
    'https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg',
    'https://youtu.be/9MjV4EwR7Mg')

RESERVOIR_DOGS = media.Movie('Reservoir Dogs',
    'After a simple jewelery heist goes terribly wrong, the surviving'
    ' criminals begin to suspect that one of them is a police informant.',
    'https://upload.wikimedia.org/wikipedia/en/f/f6/Reservoir_dogs_ver1.jpg',
    'https://youtu.be/vayksn4Y93A')


# List of defined movies we want to add to website.
MOVIES = [KINGSMAN,
    AVATAR,
    ST_INTO_DARKNESS,
    GODFATHER,
    USUAL_SUSPECTS,
    RESERVOIR_DOGS]

# Call to execute open_movies_page function from fresh_tomatoes module.
fresh_tomatoes.open_movies_page(MOVIES)
