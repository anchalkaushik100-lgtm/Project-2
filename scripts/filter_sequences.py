from Bio import SeqIO

records = list(SeqIO.parse("HSP70_sequences.fasta", "fasta"))
filtered = [r for r in records if len(r.seq) >= 100]

SeqIO.write(filtered, "HSP70_filtered.fasta", "fasta")

print("Filtered sequences:", len(filtered))
