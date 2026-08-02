VALID_BASES = {"A", "T", "C", "G"}
COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def analyze_dna(sequence: str) -> dict | None:
    """
    Analyze a DNA sequence and return its nucleotide composition.

    Args:
        sequence: A string containing a DNA sequence (A, T, C, G only).

    Returns:
        A dictionary with sequence length, nucleotide counts, GC content,
        and AT content. Returns None if the sequence contains invalid bases.
    """
    sequence = sequence.upper()

    for base in sequence:
        if base not in VALID_BASES:
            return None

    length = len(sequence)
    count_a = sequence.count("A")
    count_t = sequence.count("T")
    count_c = sequence.count("C")
    count_g = sequence.count("G")

    gc_content = ((count_g + count_c) / length) * 100 if length > 0 else 0
    at_content = ((count_a + count_t) / length) * 100 if length > 0 else 0

    return {
        "sequence": sequence,
        "length": length,
        "count_a": count_a,
        "count_t": count_t,
        "count_c": count_c,
        "count_g": count_g,
        "gc_content": gc_content,
        "at_content": at_content
    }


def reverse_complement(sequence: str) -> str:
    """
    Compute the reverse complement of a DNA sequence.

    Args:
        sequence: A valid DNA sequence.

    Returns:
        The reverse complement as a string (e.g. "ATCG" -> "CGAT").
    """
    sequence = sequence.upper()
    result = ""
    for base in reversed(sequence):
        result = result + COMPLEMENT[base]
    return result


def transcribe_to_rna(sequence: str) -> str:
    """
    Transcribe a DNA sequence into RNA by replacing T with U.

    Args:
        sequence: A valid DNA sequence.

    Returns:
        The RNA sequence as a string (e.g. "ATCG" -> "AUCG").
    """
    sequence = sequence.upper()
    return sequence.replace("T", "U")


def find_pattern(sequence: str, pattern: str) -> list[int] | None:
    """
    Find all starting positions of a pattern within a DNA sequence.

    Args:
        sequence: A valid DNA sequence to search within.
        pattern: A short DNA sequence to search for.

    Returns:
        A list of starting indices where the pattern was found.
        Returns None if the pattern contains invalid bases.
    """
    sequence = sequence.upper()
    pattern = pattern.upper()

    for base in pattern:
        if base not in VALID_BASES:
            return None

    positions = []
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions


def main():
    sequence = input("Enter a DNA sequence: ")
    result = analyze_dna(sequence)

    if result is None:
        print("❌ Error: Invalid DNA sequence. Only A, T, C and G are allowed.")
        return

    print("\n========== DNA ANALYSIS ==========")
    print(f"Sequence   : {result['sequence']}")
    print(f"Length     : {result['length']}")
    print()
    print(f"A : {result['count_a']}")
    print(f"T : {result['count_t']}")
    print(f"C : {result['count_c']}")
    print(f"G : {result['count_g']}")
    print()
    print(f"GC Content : {result['gc_content']:.2f}%")
    print(f"AT Content : {result['at_content']:.2f}%")

    rev_comp = reverse_complement(result['sequence'])
    print(f"\nReverse Complement : {rev_comp}")

    rna = transcribe_to_rna(result['sequence'])
    print(f"RNA Transcript      : {rna}")

    pattern = input("\nEnter a pattern to search for (or press Enter to skip): ")
    if pattern:
        positions = find_pattern(result['sequence'], pattern)
        if positions is None:
            print("❌ Invalid pattern. Only A, T, C and G are allowed.")
        elif positions:
            print(f"Pattern '{pattern.upper()}' found at position(s): {positions}")
        else:
            print(f"Pattern '{pattern.upper()}' not found.")

    print("=================================")


if __name__ == "__main__":
    main()