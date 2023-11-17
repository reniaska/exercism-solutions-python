# https://exercism.org/tracks/python/exercises/house

CONTENTS = [
    ("house", "Jack built."),
    ("malt", "lay in"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow with the crumpled horn", "tossed"),
    ("maiden all forlorn", "milked"),
    ("man all tattered and torn", "kissed"),
    ("priest all shaven and shorn", "married"),
    ("rooster that crowed in the morn", "woke"),
    ("farmer sowing his corn", "kept"),
    ("horse and the hound and the horn", "belonged to")]


def recite_verse(verse):
    if verse == 1:
        return CONTENTS[verse - 1][0] + " that " + CONTENTS[verse - 1][1]
    return CONTENTS[verse-1][0] + " that " + CONTENTS[verse-1][1] + " the " + recite_verse(verse - 1)


def recite(start_verse, end_verse):
    rhyme = []
    entry = "This is the "
    for verse in range(start_verse, end_verse + 1):
        rhyme.append(entry + (recite_verse(verse)))
    return rhyme
