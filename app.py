from tkinter import filedialog
from tkinter import Tk
from tkinter import *
from Bio import SeqIO

root = Tk()
root.fileName = filedialog.askopenfilename(filetypes=(
    ("fasta files", "*.fasta"), ("All files", "*.*")))

for sequence in SeqIO.parse(root.fileName, "fasta"):
    print(sequence.id)
    print(repr(sequence.seq))
    print(len(sequence))

download = Tk()
download.fileName = filedialog.askdirectory()

seq_type = input("Is this DNA (1) or Protein (2)?")
if seq_type == "1":
    dna_type = input("Is this genomic (1) or transcript (2)")
    if dna_type == "1":
        extension = "genomic"
    else:
        extension = "transcript"
else:
    extension = "protein"

for sequence in SeqIO.parse(root.fileName, "fasta"):
    SeqIO.write(sequence, download.fileName + '/' +
                sequence.id + "_" + extension + '.fasta', 'fasta')
