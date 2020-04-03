def gc_Count (seq):
    nucleotide= {"A": 0, "C": 0, "T": 0, "G": 0}
    for nuc in seq:
        if nuc in nucleotide:
            nucleotide[nuc] += 1
    percent_gc = 100* (nucleotide["G"] + nucleotide["C"]) / (nucleotide["G"] + nucleotide["C"] + nucleotide["A"] + nucleotide["T"])
    return round(percent_gc, 10)

file  = open("rosalind_gc.txt", 'r')
lines = file.readlines()
dnaDict = {}
for line in lines:
    if ">" in line:
        name = line.replace(">", "").replace("\n", "")
        dnaDict[name] = ''
    else:
        dnaDict[name] +=line

for key in dnaDict:
    seq = dnaDict[key]
    dnaDict[key] = gc_Count(seq)

for key, value in dnaDict.items():
    print (key,value)