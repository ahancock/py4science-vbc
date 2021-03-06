import subprocess

from Bio import Entrez, SeqIO, AlignIO
from Bio.Emboss.Applications import NeedleCommandline

Entrez.email = "stowers@imp.ac.at"

handle = Entrez.efetch(db="nucleotide", id="AF182035",rettype="gb", retmode="text")
homo = SeqIO.read(handle, "genbank")

handle = Entrez.efetch(db="nucleotide", id="AY863830",rettype="gb", retmode="text")
drosophila = SeqIO.read(handle, "genbank")

open("homo.fasta","w").write(homo.format("fasta"))
open("drosophila.fasta","w").write(drosophila.format("fasta"))

cmdline = NeedleCommandline(
            asequence="homo.fasta",
            bsequence="drosophila.fasta",
            gapopen=10, gapextend=0.5, outfile="needle.txt")
subprocess.call(str(cmdline), shell=True)

align = AlignIO.read("needle.txt", "emboss")
print align

