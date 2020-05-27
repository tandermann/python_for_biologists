import re
from Bio import AlignIO, SeqIO
from Bio.Seq import Seq
import argparse

# This section defines the input options. You can copy and modify this section for future scripts, it's very handy! In that case don't forget to import the argparse package (import argparse)
# Get arguments
def add_arguments(parser):
    parser.add_argument(
        '--input',
        required=True,
        default=None,
        help='Path to your input alignment file.'
    )
    parser.add_argument(
        '--input_format',
        choices=["fasta","nexus","stockholm","phylip","clustal","emboss","phylip-sequential","phylip-relaxed","fasta-m10","ig","maf"],
        required=True,
        help='Alignment format of input file.'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='Name of output alignment.'
    )
    parser.add_argument(
        '--output_format',
        choices=["fasta","nexus","stockholm","phylip","clustal","phylip-sequential","phylip-relaxed","maf"],
        required=True,
        help='Desired alignment format of output file.'
    )
    parser.add_argument(
        '--fix_invalid_characters',
        action='store_true',
        default=False,
        help='Replace all invalid bases (not A,C,T,G,a,c,t,g,-) with "N"'
    )
parser = argparse.ArgumentParser()
add_arguments(parser)
args = parser.parse_args()


# !!!!!!!!!!!!NOTE:!!!!!!!!!!!!!! You can call the input variables in the following manner: args.name_of_variable,
# e.g. input_file = args.input, input_format = args.input_format, etc.


#_________________________________________________
# Insert a function here, which replaces all invalid characters with N's

def replace_bad_chars(alignment):
	'...your code here...'
#_________________________________________________



# 1. read the alignment, using the AlignIO.read() function
alignment=AlignIO.read()

# 2. apply the function you defined above, in case the fix_invalid_characters option is activated
if args.fix_invalid_characters:
	replace_bad_chars(alignment)

# 3. write the alignment to the defined output file (args.output) using the SeqIO.write() function
SeqIO.write()

print('\n\nNew alignment written to file %s\n\n' %args.output)