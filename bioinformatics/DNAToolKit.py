import collections

nucliotides = ["A", "C", "G", "T"]
reverseCom = {"A": "T", "C":"G", "G":"C", "T":"A"}
DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}


def validateSeq(dnaSeq):
    tempSeq = dnaSeq.upper()
    for nuc in tempSeq:
        if nuc not in nucliotides:
            print("not valid")
            return False
    return tempSeq


def countNucFrequency(seq):
    tempSeqDict = {"A": 0, "C": 0, "T": 0, "G": 0}
    for nuc in seq:
        tempSeqDict [nuc] += 1
    return tempSeqDict

    #return dict(collections.Counter(seq))         easier way to do what is done in  countNucFrewuency

def dnaToRna(seq):
    return seq.replace("T", "U")


def reverseComplement (seq):
    string2 = ''
    for nuc in seq:
        string = reverseCom[nuc]
        string2 +=string
    return string2[::-1]

    #return ''.join([reverseCom[nuc] for nuc in seq]) [::-1])



def gc_Count (seq):
    nucleotide: {"A": 0, "C": 0, "T": 0, "G": 0}
    for nuc in seq:
        if nuc in nucleotide:
            nucleotide[nuc] += 1
    percent_gc = (nucleotide["G"] + nucleotide["C"]) / (nucleotide["G"] + nucleotide["C"] +nucleotide["A"] + nucleotide["T"])
    return nucleotide


def transRNAtoProtein(seq):
    seq = seq.replace("U","T")
    length = len(seq)
    string = ''
    protein = ''
    for x in range(int(length/3)):
        for y in range(3):
            string += seq[x*3 + y]
        string = DNA_Codons[string]
        protein += string
        string = ''
    print (protein)

def RNAtoProtein(seq, init_pos=0):  #simpilar code of transRNAtoProtein
     seq = seq.replace("U","T")
     return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) -2, 3)]


def readingFrames(seq):
    reverseSeq = seq[::-1]
    frames = []
    reverseFrames = []
    for x in range(0,3):
        frames.append(RNAtoProtein(seq, x))
        reverseFrames.append(RNAtoProtein(seq, x))

    return frames, reverseFrames


def proteinInReadingFrame(AA_sequence):
    proteins = []
    oneProtein = ''
    for i in range(len(AA_sequence)):
        oneProtein += AA_sequence[i]
        if AA_sequence[i] == '_':
            proteins.append(oneProtein.replace(' ', ''))
            oneProtein = ''
        elif oneProtein[0] == 'M':
            oneProtein += AA_sequence[i]
        if AA_sequence[i] == 'M':
            oneProtein += AA_sequence[i]
    return proteins

