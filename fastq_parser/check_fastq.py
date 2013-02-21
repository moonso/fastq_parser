#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Måns Magnusson on 2013-02-21.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from Bio import SeqIO
from fastq_sequence import fastq_record


def guess_quality(infile):
	"""Guess which quality meassure is beeing used."""
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


def main():
	infile = sys.argv[1]
	print guess_quality(infile)
	# handle = open(infile,'rU')
	# for seq_record in SeqIO.parse(infile, 'fastq'):
	# 	print seq_record.id
	# 	print len(seq_record)
	# 	print seq_record


if __name__ == '__main__':
	main()

