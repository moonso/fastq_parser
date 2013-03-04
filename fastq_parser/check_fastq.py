#!/usr/bin/env python
# encoding: utf-8
"""
check_fastq.py

Take a fastq file as input and checks if the quality string is in the PHRED+33 format or not.
If --convert the qualities are converted to sanger(PHRED+33) format.

Created by Måns Magnusson on 2013-02-21.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import argparse
from Bio import SeqIO
from fastq_sequence import fastq_record


def guess_quality(infile):
	"""Guess which quality meassure is beeing used. Goes through the record of sequences until one with unquetionable information is found and then stops."""
	i = 1
	info = {}
	for line in open(infile, 'r'):
		line = line.rstrip()
		if i < 5:
			if i % 4 == 0:
				info['qualitystring'] = line
			elif i % 3 == 0:
				info['info_string'] = line
			elif i % 2 == 0:
				info['sequence'] = line
			else:
				info['id_string'] = line
		else:
			fastq_sequence = (fastq_record(**info))
			fastq_sequence.guess_quality()
			if fastq_sequence.format:
				return fastq_sequence.format
			i = 1
			info = {}
			info['id_string'] = line
		i += 1
	return 'Not clear'

def convert_quality_scores(infile, outfile = '', qualities='illumina'):
	"""Converts the quality scores to sanger(PHRED+33)"""
	if len(outfile) < 1:
		outfile = infile+'.p33'
	SeqIO.convert(infile, 'fastq-'+qualities, outfile, 'fastq')


def main():
	parser = argparse.ArgumentParser(description="""Give the path to a file to check what quality values are beeing used.
	If argument --convert then the quality values are converted to sanger format, if necessary.
	If no outfile is specified the new file will have the same name as the infile but with the ending .p33""")
	parser.add_argument('infile', type=str, help="Specify the new infile.")
	parser.add_argument('-conv', '--convert', help="Convert the qualities to sanger format if necessary", action="store_true")
	parser.add_argument('-out', '--outfile', help="Specify the outfile", default='')
	args = parser.parse_args()
	infile = args.infile
	outfile = args.outfile
	if os.path.exists(infile):
		if os.path.isfile(infile):
			pass
		else:
			print infile, ' is not a file!'
			sys.exit()
	else:
		print infile, ' does not exist!'
		sys.exit()
	quality = guess_quality(infile)
	if quality == 'illumina':
		if args.convert:
			convert_quality_scores(infile, outfile, quality)
	# handle = open(infile,'rU')
	# for seq_record in SeqIO.parse(infile, 'fastq'):
	# 	print seq_record.id
	# 	print len(seq_record)
	# 	print seq_record


if __name__ == '__main__':
	main()

