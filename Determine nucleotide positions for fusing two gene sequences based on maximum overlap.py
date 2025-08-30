
def find_max_overlap(seq1, seq2):
    min_len = min(len(seq1), len(seq2))
    max_overlap = 0
    for k in range(1, min_len):
        if seq1[-k:] == seq2[:k]:
            max_overlap = k
    return max_overlap


seq1 = input("Enter the sequence of the first gene: ").strip().upper()
seq2 = input("Enter the sequence of the second gene: ").strip().upper()


max_overlap = find_max_overlap(seq1, seq2)


position1 = len(seq1)
position2 = max_overlap + 1


fused = seq1 + seq2[max_overlap:]

print(f"The two genes can be combined at position {position1} of the first gene and position {position2} of the second gene to form a fused gene.")
print(f"Fused gene sequence: {fused}")
print(f"Overlap length: {max_overlap}")

