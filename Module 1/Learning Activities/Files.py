#Read and Write from file the % of C and G nucleotides in a DNA Sequence

def calculate_cg_percentage(dna_sequence):
    total_length = len(dna_sequence)
    count_c_g = dna_sequence.count("C") + dna_sequence.count("G")
    cg_percentage = (count_c_g / total_length) * 100
    return cg_percentage

#Open the input DNA file for processing

with open ('dna.txt', 'r') as input_file:
    #Open the output file for writing
    with open('output_cg_percentage.txt', 'w') as output_file:
        #Process each line in file
        for line in input_file:
            #Calculate the percentage of C and G nucleotides
            cg_percentage = calculate_cg_percentage(line.strip())
            print("The Percentage of C&G nucleotides is", cg_percentage)

            #write the count to the output file
            output_file.write(f"The percentage of C + G in DNA sequence is: {cg_percentage:.2f}%\n")