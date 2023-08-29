def reverse_lines1(input_file, output_file):
    with open(input_file) as f, open(output_file, 'w') as of:
        for line in f:
            of.write(line.rstrip()[::-1])
            of.write("\n")

def reverse_lines(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')


reverse_lines('./input_ex24.txt', './output_ex24.txt')