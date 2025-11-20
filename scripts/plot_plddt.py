import json
import numpy as np
import matplotlib.pyplot as plt

with open("full_data.json") as f:
    data = json.load(f)

plddt = np.array(data["atom_plddts"])

plt.figure(figsize=(10,4))
plt.plot(plddt)
plt.title("pLDDT Confidence Scores")
plt.xlabel("Residue Index")
plt.ylabel("pLDDT")
plt.savefig("plddt_plot.png", dpi=300)
