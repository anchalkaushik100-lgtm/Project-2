Project 2 – Protein Sequence Analysis & Structure Prediction

This repository contains all scripts, data files, results, and the final report for Project 2.  
The project involves sequence retrieval, multiple sequence alignment, phylogenetic analysis,  
tertiary structure prediction using AlphaFold, confidence analysis (pLDDT & PAE), and structural  
validation using PROCHECK.

Project Workflow Overview

Sequence Retrieval
- Retrieved Heat Shock Protein 70 (HSP70) sequences from NCBI.
- Filtering was done to keep only complete, non-redundant sequences.

Files:
- `sequences/HSP70_sequences.fasta`
- `sequences/HSP70_filtered.fasta`
- `sequences/merged_10_sequences.fasta`


Multiple Sequence Alignment (MSA)
Performed using Clustal Omega.

Commands:
- `clustalo -i merged_10_sequences.fasta -o msa_clustalo.fasta --outfmt=fa`
- Converted to `.phy` and `.aln` formats.

Files:
- `msa/msa_clustalo.fasta`
- `msa/msa_clustalo.aln`
- `msa/msa_clustalo.phy`


Phylogenetic Tree Construction (PhyML)
Performed maximum likelihood (ML) tree with 100 bootstraps.

Command:
- `phyml -i msa_clustalo.phy -d aa -b 100`

Model used: LG + Gamma (4 categories), I=0  
Files:
- `phyml/msa_clustalo.phy_phyml_tree.txt`
- `phyml/msa_clustalo.phy_phyml_stats.txt`
- `phyml/bootstraps/`


Tertiary Structure Prediction (AlphaFold2/ColabFold)
Two sequences were selected:
- Model 1:Nypamodiolus japonicus
- Model 2:** *Bathymodiolinae sp.

Outputs include:
- `.cif` structure files  
- pLDDT scores (JSON)  
- PAE matrices  
- 3D structure PNG  
- Unrelaxed and relaxed PDB files  

Files: 
Inside:
- `alphafold_model1/`
- `alphafold_model2/`


pLDDT & PAE Plotting
Extracted using Python from JSON files.

Script:
- `scripts/plot_plddt.py`


Structure Validation (PROCHECK)
Ramachandran plot & other stereochemical parameters checked.

Files:
- `procheck/ramachandran.png`
- `procheck/residue_props.png`


Final Report
Contains all answers, workflow, explanation, figures,  
and results.
File:
- `final_report/Project2_Anchal.pdf`



Repository Structure
Project-2/
│
├── sequences/
├── msa/
├── phyml/
├── alphafold_model1/
├── alphafold_model2/
├── procheck/
├── scripts/
└── final_report/

GitHub Link
All files are available in this repository:  
**https://github.com/anchalkaushik100-lgtm/Project-2**

