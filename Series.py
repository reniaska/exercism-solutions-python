#https://exercism.org/tracks/python/exercises/series

def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif len(series) == 0:
        raise ValueError("series cannot be empty")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    else:
        return [series[i:i+length] for i in range(len(series)-length+1)]