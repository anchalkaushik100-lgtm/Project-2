import requests
import time

fasta = open("merged_10_sequences.fasta").read()

# Submit job
r = requests.post("https://www.ebi.ac.uk/Tools/services/rest/clustalo/run/",
                  data={"email": "your_email@example.com", "sequence": fasta})
job_id = r.text
print("JOB ID:", job_id)

# Wait for job to finish
while True:
    status = requests.get(f"https://www.ebi.ac.uk/Tools/services/rest/clustalo/status/{job_id}").text
    print("Status:", status)
    if status == "FINISHED":
        break
    time.sleep(5)

# Fetch alignment in FASTA format
alignment = requests.get(
    f"https://www.ebi.ac.uk/Tools/services/rest/clustalo/result/{job_id}/fa"
).text

with open("msa_clustalo.fasta", "w") as f:
    f.write(alignment)

print("Saved msa_clustalo.fasta")
