# https://exercism.org/tracks/python/exercises/etl


def transform(legacy_data):
    data = {}
    for key in legacy_data:
        for letter in legacy_data[key]:
            data[letter.lower()] = key
    return data
