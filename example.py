# example.py
# Code to print top 20 popular shows

from tmdbwrapper import TV

popular = TV.popular()

for number, show in enumerate(popular['results'], start=1):
    print("{num}. {name} - {pop}".format(num=number,
                                         name=show['name'], pop=show['popularity']))