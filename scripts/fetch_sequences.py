from Bio import Entrez, SeqIO

Entrez.email = "your_email@example.com"   # replace with your email

search_handle = Entrez.esearch(db="protein", term="HSP70", retmax=200)
search_results = Entrez.read(search_handle)
ids = search_results["IdList"]
search_handle.close()

fetch_handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
records = list(SeqIO.parse(fetch_handle, "fasta"))
fetch_handle.close()

SeqIO.write(records, "HSP70_sequences.fasta", "fasta")

print("Downloaded", len(records), "sequences.")
