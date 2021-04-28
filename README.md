# randomizers V0.1
A practice project of randomizing random things I think would be amusing or practical.

Project goals:
1.0 - the basic randomizers I have either re-coded over time with failed starts, and a couple new ones I thought of, programmed in Python for pure CLI interface with minimal error handling.
2.0 - Expand to GUI with PyQT5, executeables and maybe web integration.
3.0 - Expand to phone interface

As it is now, the randomizers are as follows:

Magic 8-ball: returns a random result from a list of all Magic 8-ball answers.
Random phrases: pulls a random line from a text file. Currently just a couple dumb things I shoved it, could be any text. Mostly thought I'd put in reandom quotes.
Random location: Comes up with a random location, with guidance on setting, style, and what lives there.
Random genre: I want to populate the list with more words, but taking the trend of terms like "steampunk, cyberpunk, dieselpunk, ETC" I made a randomizer that added "punk" to a random list of words so that I could have more genres to work with. It was my intention to replace "punk" with other words as well, but the results for what the genre could possibly be became too esoteric.
Random character: lots of research into fashion styles, and searching for usable lists online to plug into the code so that I have hundreds of possible results for a single given return, rather than what I could think of or find. Just something novel I thought I may try to solicit to artists to see how they like it or what they do.
Random game: a random game idea. Currently haven't coded this one, as I am still undecided on how it would be expressed. What random prompts would be given. Currently thinking along the ideas of: genre, random word like you'de get for a jam project, random "mechanic" which is just a list of basic ideas that are mostly non-standard for what to do with gameplay.

As this is the version I am first uploading of it in this current form, I'm calling this version 0.1.

Current goals:
1. Add an error check for whether a species has legs, and skip bottom clothing for legless species on the random character generator. The error check function is in, but I haven't sat down and considered how to re-work the output character to remove it, as that will require some revision due to how the code currently inserts the random results into the final form.
2. Expand on the various lists with more words. Focus on the various clothing lists, as well as the genre randomizer in particular.
3. Come up with a proper answer for what the "random game generator"'s results would look like, and begin forming lists for it.
4. Recode the random location generator. I largely patched in old programming, but after starting on the character generator, I liked its format of "outfit style: asdf, outfit: asdf" much more than the attempt at compiling the results into a sentence.
