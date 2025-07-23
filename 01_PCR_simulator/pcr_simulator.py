def read_dna_sequence(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        dna = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return dna

def denature(dna):
    return dna # Dna is split, but since it is single-stranded in text, we leave it as is

def anneal_primer(dna,primer):
    return primer in dna

def extend(primer, dna):
    start = dna.find(primer)
    if start != -1:
        return dna[start:]
    else:
        return "Primer not found in sequence"

# Simulate one cycle
dna = read_dna_sequence("example_input.fasta")
primer = "ATGC" # Your starting point

print("Original Dna:", dna)
print("Primer Found:", anneal_primer(dna,primer))
print("Extended Strand:", extend(primer, dna))
