def motif(str1, str2):
    result = []
    for i in range(0, len(str1) - len(str2)):
        if str1[i:i + len(str2)] == str2:
            result.append(i + 1)
    return result


results = str(motif('ATCGTACGTGCGTACGTGTGTACGTGTGTACGTGGGGTACGTGGTACGTGCATATGTACGTGCGTACGTGTCATTGTACGTGGCGCTACGCCGTACGTGGTACGTGGTACGTGTGCGTACGTGTGTACGTGGTACGTGGTACGTGGCGTACGTGGGTACGTGTTTAGGTACGTGCCCGTACGTGGCTGAGTCAGTACGTGGTACGTGGAGTACGTGCGTACGTGCGTACGTGGGGTACGTGTTTCTGGTACGTGAGTACGTGCGATGCGGCAGTGTACGTGGTGTACGTGGGGTACGTGTGTACGTGCGTACGTGGTACGTGCCCCTCGTACGTGTCGCGTACGTGAACCTCGTACGTGAGGAATTTCGTACGTGGTACGTGGTACGTGAGTACGTGAGTACGTGAGGTACGTGATTTTGTACGTGGTTCTAGTACGTGGTACGTGGCCGTACGTGGTACGTGGTACGTGGTACGTGAGTACGTGACGCGACGCTCAGTACGTGGTACGTGGTAGTACGTGATCAATTGTGGCGTACGTGTCCCAAGTACGTGGTACGTGGTACGTGGTACGTGGTGGGGTACGTGGGTACGTGGTACGTGGTACGTGTCGGCCTGGTGTACGTGACGTACGTGGTACGTGGCGTACGTGGGCGGTACGTGGTACGTGTGTACGTGCCCAACGGTACGTGGTACGTGGTACGTGTGTACGTGGTACGTGGTACGTGAGTACGTGGCGTACGTGGGCGCCTCCAAGAGGAGGTACGTGATTTTGTACGTGACTCGACAAGAGGTACGTGGTGTACGTGTCGTACGTGGTACGTGTGGTACGTGGTACGTGATGTACGTGTGGTACTTCGTACGTGAAGTACGTGCACGGCGTACGTGTTTGTACGTGGGTACGTGGTACGTGGTGGAGTACGTGTTCCTGAAGGCGTACGTGAGTACGTG', 'GTACGTGGT'))

y = results.replace("[", "").replace("]", "").replace(",", "")
print(y)
