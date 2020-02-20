#ex2
from pathlib import Path

def seq_read(filename):
    file_contents= Path(filename).read_text() #read the file
    seq_dna=file_contents
    index_finish= seq_dna.find("\n")
    seq_dna= seq_dna[index_finish +1:]
    seq_dna=seq_dna.replace("\n", "")
    seq_dna=seq_dna[:20]
    return seq_dna

#ex3

def seq_len(filename):
    return len(filename)

def seq_read2(filename):
    c= Path(filename).read_text()
    b=c.split("\n")[1:]
    return "".join(b)

#ex4

def seq_count_bases(seq, b):
    return seq.count(b)

#ex5
def count(seq):
    e={"A": seq_count_bases(seq, "A"), 'T': seq_count_bases(seq, 'T'),
           'C': seq_count_bases(seq, 'C'), 'G': seq_count_bases(seq, 'G')}
    return e

#ex6

def seq_reverse(seq):
    return seq[::-1]

#Ex7

def seq_complement(seq):
    e = {"A": "T", 'T':'A', 'C':'G', 'G' :'C'}
    r=""
    for b in seq:
        r += e[b]
    return r




