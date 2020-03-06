from pathlib import Path

# ex1


def seq_ping():
    print("Testing the seq_ping() funcion", "\n", "OK")

# ex2


def seq_read_fasta(filename):
    #  read the text
    content = Path(filename).read_text()
    space = content.find("\n")
    #  remove the head
    content = content[space + 1:]
    #  remove the black spaces
    content = content.replace("\n", "")

    return content

# ex3


def seq_len(filename):
    return len(filename)

# ex4


def seq_count_base(filename, b):
    # counting the base on the sequence
    return filename.count(b)

# ex5


def count(sequence):
    # creating a dictionary with the number of each base
    bases = {'A': seq_count_base(sequence, 'A'), 'T': seq_count_base(sequence, 'T'),
             'C': seq_count_base(sequence, 'C'), 'G': seq_count_base(sequence, 'G')}
    return bases

# ex6


def seq_reverse(sequence):
    return sequence[::-1]

# ex7


def seq_complement(sequence):
    # we create a dictionary implementing the complementary and then,
    # we travel around it
    c = {"A": "T", 'T': 'A', 'C': 'G', 'G': 'C'}
    r = ""
    for b in sequence:
        r += c[b]
    return r
