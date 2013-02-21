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




def main():
	infile = sys.argv[1]
	handle = open(infile,'rU')
	for seq_record in SeqIO.parse(infile, 'fastq'):
		print seq_record.id
		print len(seq_record)
		print seq_record


if __name__ == '__main__':
	main()

