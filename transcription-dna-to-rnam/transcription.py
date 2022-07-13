dna_file = open('dna_file.txt', 'r').read()
rna_file = open('rna_file.txt', 'w')

transcription_code = {
	'A':'U',
	'T':'A',
	'G':'C',
	'C':'G'
}

for letter in dna_file:
	rna_file.write(str(transcription_code.get(letter)))

rna_file.close()