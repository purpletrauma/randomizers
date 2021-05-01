# randomizers V0.2
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

Random game: a random game idea. Currently haven't coded this one, as I am still undecided on how it would be expressed. What random prompts would be given. Currently thinking along the ideas of: genre, random word like you'de get for a jam project, random "mechanic" which is just a list of basic ideas that are mostly non-standard for what to do with gameplay.

Current goals:
1. Expand on the various lists with more words. Focus on the various clothing lists, as well as the genre randomizer in particular.
2. Come up with a proper answer for what the "random game generator"'s results would look like, and begin forming lists for it.
3. Add new lists for either the game generator, or potential future randomizer ideas. Those unpopulated lists are: videogame genres, videogame mechanics, videogame tags. I also would like one for greek words that is a dictionary datatype so that it can be translated on the fly. So that I can pick a random one, add "philia" or "phobia" and provide translation. Maybe more later if I can wrap my head around methodologies for scientific taxonomy of various purposes. It is a somewhat vague topic to look up on its own.
4. If I expand into basic Python machine learning libraries, could I scour, say, imdb of its films using a script, create designated datasets for the film summary, quotes section, actors sections, ETC, and see what it comes up with when I run several independent AI into creating a complete profile for a fictional film? An idea for later, possibly after I hit 2.0.
