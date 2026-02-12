def parse_fasta(file_path):
	sequences = {}
	current_header = None

	with open(file_path , "r") as file:
		for line in file:
			line = line.strip()
			if line.startswith(">"):
				current_header = line[1:]
				sequences[current_header] = ""
			else:
				sequences[current_header] += line

	return sequences

def gc_content(sequence):
	g = sequence.count("G")
	c = sequence.count("C")
	return (g + c) / len(sequence) * 100

def analyze_sequences(sequences):
	lengths = []
	gc_values = []

	for header, sequence in sequences.items():
		lengths.append(len(sequence))
		gc_values.append(gc_content(sequence))

	print(f"Total sequences: {len(sequences)}")
	print(f"Average length: {sum(lengths)/len(lengths):.2f}")
	print(f"Longest sequence: {max(lengths)}")
	print(f"Shortest sequence: {min(lengths)}")
	print(f"Overall GC content: {sum(gc_values)/len(gc_values):.2f}%")

if __name__ == "__main__":
	fasta_file = "sample.fasta"
	sequences = parse_fasta(fasta_file)
	analyze_sequences(sequences)

