# FASTA Sequence Analyzer

A lightweight Python tool for parsing and analyzing biological sequence data in FASTA format.

This project was built as a foundational bioinformatics scripting exercise to demonstrate command-line workflow, file parsing, and basic sequence statistics analysis.

---

## 🧬 Features

- Parses multi-sequence FASTA files
- Calculates:
  - Total number of sequences
  - Average sequence length
  - Longest sequence
  - Shortest sequence
  - Average GC content
- Handles empty FASTA files safely

---

## 📂 Example FASTA Input

seq1
ATGCGTACGTAGCTAGCTAG
seq2
GGGCGCGTTTAAACCCGGG
seq3
ATATATATATATATATATA

---

## 📊 Example Output
Total sequences: 3
Average length: 19.33
Longest sequence: 20
Shortest sequence: 19
Overall GC content: 39.47%

---

## 🚀 How To Run

Clone the repository:

```bash
git clone https://github.com/gmansuperman/fasta-sequence-analyser.git
cd fasta-sequence-analyser

Run the script
python3 seq_analyser.py


Make sure your FASTA file is named sample.fasta or modify the filename inside the script.

---

## Tech Stack

Python 3

Command-line workflow

Git & GitHub version control

---
## Future Improvements

Add command-line argument support

Support large FASTA files efficiently

Add nucleotide frequency breakdown

Add N-content calculation

Export results to CSV

Integrate with Biopython

---
## Author

Kristian Gonzales
BSc Microbiology | Master of Bioinformatics
University of Guelph
