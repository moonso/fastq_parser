#!/usr/bin/env python
# encoding: utf-8
"""
fastq_sequence.py

Created by Måns Magnusson on 2013-02-21.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os

class fastq_record(object):
	"""Holds the information of a fastqsequence"""
	def __init__(self, id_string = '.', sequence = '.', info_string = '.', qualitystring = '.'):
		super(fastq_record, self).__init__()
		self.id_string = id_string
		self.sequence = sequence
		self.info_string = info_string
		self.qualitystring = qualitystring
		self.format = None # Options are 'solexa', 'illumina', 'sanger'
	
	def guess_quality(self):
		"""Guess which quality meassure that is used for this fastq_file"""
		for qual in self.qualitystring:
			if ord(qual) < 59:
				self.format = 'sanger'
				break
			elif ord(qual) > 80:# The scores rarely exceeds 40 (33+40=77) so with a score over 80 we can be pretty confident on illumina.
				self.format = 'illumina'
				break
	
	def print_sequence(self):
		"""Prints the sequence in fastq format"""
		print self.id_string
		print self.sequence
		print self.info_string
		print self.qualitystring

def main():
	infile = sys.argv[1]
	i = 1
	info = {}
	my_sequences = []
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
			my_sequences.append(fastq_record(**info))
			i = 1
			info = {}
			info['id_string'] = line
		i += 1
	for seq in my_sequences:
		seq.guess_quality()
				


if __name__ == '__main__':
	main()

