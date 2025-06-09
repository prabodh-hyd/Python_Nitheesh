def to_rna(dna_strand):
    rna_converting = {'G':'C', 'T':'A', 'A':'U', 'C':'G'}

    return ''.join(rna_converting[n] for n in dna_strand)
