# randomizers
A practice project of randomizing random things I think would be amusing or practical.

Project goals:
1.0 - the basic randomizers I have either re-coded over time with failed starts, and a couple new ones I thought of, programmed in Python for pure CLI interface with minimal error handling.
2.0 - Expand to GUI with PyQT5, executeables and maybe web integration.
3.0 - Expand to phone interface

As it is now, the randomizers are as follows:

Magic 8-ball: returns a random result from a list of all Magic 8-ball answers.

Random phrases: pulls a random line from a text file. Currently just a couple dumb things I shoved in, could be any text. Mostly thought I'd put in random quotes.

Random location: Comes up with a random location, with guidance on setting, style, and what lives there.

Random genre: I want to populate the list with more words, but taking the trend of terms like "steampunk, cyberpunk, dieselpunk, ETC" I made a randomizer that added "punk" to a random list of words so that I could have more genres to work with. It was my intention to replace "punk" with other words as well, but the results for what the genre could possibly be became too esoteric.

Random character: generates a random character with a species, age, gender, outfit style, outfit, personality, two colors, quirk, and if chosen to turn on, a kink. Found that last one kinda amusing.

Random game: a random game prompt. Currently haven't coded this one, but close to settling on what it will do. It will have light/medium/heavy modes. It is meant to be a prompt generator and not a game generator, so it never gives a specific game but things to work off of for game concepts. Light = basic prompt to run with like what you would get from most game jams. Medium = Light + existing randomizers to give you some setting and style, like how the "genre" section works for the location generator. Heavy = Medium + randomized idea for a unique gameplay style. Considering making the "silly mode" default here rather than needing to ask for extra adjectives, since the whole idea is to come up with unique prompts that force you to adapt without telling you what you're making.

Current goals:
1. The randomizers could always use more lists, or more items in the lists. Expanding upon the content and options is always a perpetual to-do item.
2. If I expand into basic Python machine learning libraries, could I scour, say, imdb of its films using a script, create designated datasets for the film summary, quotes section, actors sections, ETC, and see what it comes up with when I run several AI processes designated to specific sections, creating a complete profile for a fictional film? An idea for later, possibly after I hit 2.0. Machine Learning is on the periphery of packages I wish to try, and that sounds like an amusing one.
