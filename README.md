# DNA Sequence Analyzer

A Python project for performing basic DNA sequence analysis. This project was built as part of my journey to learn Python and apply programming to biotechnology and bioinformatics.

## Features

- Validate DNA sequences (A, T, C, G)
- Count nucleotide frequencies (A, T, C, G)
- Calculate GC content
- Calculate AT content
- Generate the reverse complement
- Transcribe DNA to RNA
- Search for DNA sequence patterns (motifs)

## Technologies Used

- Python 3

## Project Structure

```
dna_sequence_analyzer.py
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/abdullahhrma/dna-sequence-analyzer.git
```

2. Navigate to the project directory:

```bash
cd dna-sequence-analyzer
```

3. Run the program:

```bash
python dna_sequence_analyzer.py
```

## Example

**Input**

```
Enter a DNA sequence:
ATCGATCG
```

**Output**

```
========== DNA ANALYSIS ==========
Sequence   : ATCGATCG
Length     : 8

A : 2
T : 2
C : 2
G : 2

GC Content : 50.00%
AT Content : 50.00%

Reverse Complement : CGATCGAT
RNA Transcript      : AUCGAUCG
```

## Future Improvements

- Read DNA sequences from FASTA files
- DNA to protein translation
- Restriction enzyme recognition
- Sequence alignment
- Additional sequence statistics

## About

This project is part of my **Python for Biotechnology** learning journey, where I build practical Python applications related to biology and bioinformatics.