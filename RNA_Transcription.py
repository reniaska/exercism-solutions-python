#https://exercism.org/tracks/python/exercises/rna-transcription

def to_rna(dna_strand):
    DNA = 'ACGT'
    RNA = 'UGCA'
    rna_trans = ''
    for letter in dna_strand:
        rna_trans += RNA[DNA.index(letter)]
    return rna_trans