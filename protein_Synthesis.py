# Description: https://www.codewars.com/kata/58df2d65808fbcdfc800004a
# My solution:
def protein_synthesis(dna):
    table = str.maketrans('ACGT','UGCA')
    rna_string = dna.translate(table)
    rna = [rna_string[y-3:y] for y in range(3, len(rna_string)+3, 3)]
    amino = [CODON_DICT[rna[i]] for i in range(0, len(rna)) if len(rna[i]) == 3]
    return " ".join(rna), " ".join(amino)