# Given two strings ss and tt of equal length, the Hamming distance between ss and tt, denoted dH(s,t)dH(s,t),
#  is the number of corresponding symbols that differ in ss and tt. See Figure 2.

# Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).
# Return: The Hamming distance  dH(s,t)

def findhamming(s,t):
    dist = 0
    for i in range(0, len(s)):
        if s[i]!=t[i]:
            dist+=1
    return dist

s = 'TACCTGGGCGCCCCGGGCAGTGGTCATCTTTCGTGAATACAGGAAAGCACTGAGGCGCACACGCACAACGCTTATGCCGGACAAAATCAAGTTAGGCGTAGGCTCGCACCCATAGCCGCTCCTACAGAATATTTTAGACCGAGGGGGGAGGCAGGCGACGTCCATCTTAAATCGGGAGCGTAGTCCTTTCAACAATCAGGAATTTTGTGCCACAGGTCGTCTAGGTATCCTAATTAAGTGTTTATATGAAACGGATAGGTCAGTTCATTCATGCGTCAACCCGAACCGTAGTGAAAGTGGACTATAGATACCTGACGCTAATACCCGGGGTTCGAAACAGTCAATTTGTAGAGCAGGCGACTAGGTACTACGATGCCAGGTGTCCTAGACCCTGCATCAGAGCTCCTATTATCAGCCTGGAGAAGATCGTTTCGTTAAATCAAAAACGTCTGAATTTTTGCGCAAATGTACGTAGCCTTGGACGAGTGATTTCACTGGACCTGACGATAAATTCCTGCACATCCGTTGCGAACTAGCGCGGACGCTCCGAATAGCCGAATAACGGCTGCGTATGTTGCGCGCTTTAATCTATTCGTGTAACATGAAGCTCGCCCGGTGAGTCAAGCGGATACCATTTATAGACCAGTGAAGAAGGGCGTCATCCAAATAGTATCGCCTGCGTCAACGGCTAGATTACTTTGATAAAAGTCCGCTACAAGGTGGGCTCATTATTGGGCTAATTGGTGACTTAAGGTGCATGCGGTTTTAGGGTAAACCCGCCGACCTTTCGCGCCAGCCCACACTGCGTGATGGAAAGACTGCTTCTCTAGCGGCACGAACGCGCAGTCTCCAGGCACTCCGAGACGGGCTACGGCGATCACCGCATGCGATACCACTGTGCGACTGCCTGTGGTTGACGCCCGACCGTA'
t = 'TACCTCCCCGGCGCCTGCGCGCGTCTGGTAAATTGAATCGATGGACTATTGGAGCAGAACACGATAACCGTTGCTGACTAATTAACGGCCGCCAGCAGTTCGGGCGGAAAGCTAGCCGTGGCTAACGTCTATTGAACGGGGATGAGTACGCCAGGTTCAGACCCCCTAACAACGGATCCCGACCCGCTCCGTCAAGTAGCGGTCGTGTCTTTCTGGTAGAATATGTAGTGTGATTAGGTGTCGGTATAGGCGTGATTGGTAAGGCCATTAAAGCGGTATACCAACTCGAGTCACAGTTGGCGTCCACCACCCGGTCCGTAATCACAGAGGTGGTTAACGAGCTATCGGTAGACGATGCCTTCAGATATATGGAGGCATTCCATCCGTGTGCGTCCATGGCGTCCAAGTGTCGCAGCTTGCACACGCCCGTTTCGCCGAATGCGAGGGAGCAGGAATATACATCAACTAGACGTAGGCCGGGTCGAGTTGTCTCCGAGGACCTGATTGAAATTTTCTAAACCAGGGGTCCGAACAAGCGCGTTCGAGCCTAAGAGACCGAAAATGTCGTCGTTCGTCGCTATCTTTTCACAAGGCGGTGGATTCGGTCCAGGACGTGTGTGTCTGGGGGTTCAAGATTATGCCCAAGCGATGGTCGACGACATCGAGATAGAGCCGGCTGCCACAATGCCCTATTGGCTTTGTCTAAGATCGACTTCGAGAAGAGCACACTTCTGGGGTTCTTGGGGATGAATGGTTCATACGGAGCTAAGTCGAACCCATCGACAATTCTCGCCAGCCGCGGCTGCCAGTACCCGGAAAAGCTCCTCTTTATGAAGCGACAGGGCATATGCCGGAACTCTCAGTCGGTATATGTGCAACATGGTATGCGCTGGGTCTGACCGCCTCGCCATTGTTCCGGCGGGACAGAG'
print(findhamming(s,t))