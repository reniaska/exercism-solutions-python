# https://exercism.org/tracks/python/exercises/bottle-song

quantity = ["no",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten"]
verse_start = "{} green {} hanging on the wall,"
verse_middle = "And if one green bottle should accidentally fall,"
verse_end = "There'll be {} green {} hanging on the wall."


def recite(start, take=1):
    lyrics = []
    for verse in range(start, start - take, -1):
        bottles_start = f"bottle{'s' if verse != 1 else ''}"
        bottles_end = f"bottle{'s' if verse != 2 else ''}"
        lyrics.append(verse_start.format(quantity[verse], bottles_start))
        lyrics.append(verse_start.format(quantity[verse], bottles_start))
        lyrics.append(verse_middle)
        lyrics.append(verse_end.format(quantity[verse-1].lower(), bottles_end))
        if take > 1 and verse > start - take + 1:
            lyrics.append('')
    return lyrics
