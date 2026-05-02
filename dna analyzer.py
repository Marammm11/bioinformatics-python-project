"""
DNA Analyzer Tool
Bioinformatics mini-project
"""

def nucleotide_count(dna_sequence):
    dna_sequence = dna_sequence.upper()
    return {
        "A": dna_sequence.count("A"),
        "T": dna_sequence.count("T"),
        "G": dna_sequence.count("G"),
        "C": dna_sequence.count("C")
    }

def gc_content(dna_sequence):
    g = dna_sequence.count("G")
    c = dna_sequence.count("C")
    return (g + c) / len(dna_sequence) * 100

def dna_to_rna(dna_sequence):
    return dna_sequence.replace("T", "U")

def reverse_complement(dna_sequence):
    complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return "".join(complement[base] for base in reversed(dna_sequence))

# User input
dna = input("Enter a DNA sequence: ")

# Validation
if not all(base in "ATGC" for base in dna.upper()):
    print("Invalid DNA sequence")
else:
    print("Nucleotide count:", nucleotide_count(dna))
    print("GC Content:", gc_content(dna), "%")
    print("RNA:", dna_to_rna(dna))
    print("Reverse complement:", reverse_complement(dna))
