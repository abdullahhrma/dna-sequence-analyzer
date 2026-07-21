def analyze_dna():
    # Ask the user to enter a DNA sequence
    sequence = input("Enter a DNA sequence: ").upper()

    # Check if the sequence contains only valid DNA bases
    valid_bases = {"A", "T", "C", "G"}

    if not all(base in valid_bases for base in sequence):
        print("❌ Error: Invalid DNA sequence.")
        print("Only A, T, C and G are allowed.")
        return

    # Calculate sequence length
    length = len(sequence)

    # Count nucleotides
    count_a = sequence.count("A")
    count_t = sequence.count("T")
    count_c = sequence.count("C")
    count_g = sequence.count("G")

    # Calculate percentages
    gc_content = ((count_g + count_c) / length) * 100 if length > 0 else 0
    at_content = ((count_a + count_t) / length) * 100 if length > 0 else 0

    # Display results
    print("\n========== DNA ANALYSIS ==========")
    print(f"Sequence   : {sequence}")
    print(f"Length     : {length}")
    print()
    print(f"A : {count_a}")
    print(f"T : {count_t}")
    print(f"C : {count_c}")
    print(f"G : {count_g}")
    print()
    print(f"GC Content : {gc_content:.2f}%")
    print(f"AT Content : {at_content:.2f}%")
    print("=================================")


analyze_dna()