#https://exercism.org/tracks/python/exercises/protein-translation

codons_proteins = {'AUG': 'Methionine',
                   'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
                   'UUA': 'Leucine', 'UUG': 'Leucine',
                   'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
                   'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
                   'UGC': 'Cysteine', 'UGU': 'Cysteine',
                   'UGG': 'Tryptophan'}


def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    proteins_list = []
    for codon in codons:
        if codon not in ('UAG', 'UAA', 'UGA'):
            proteins_list.append(codons_proteins[codon])
        else:
            break
    return proteins_list