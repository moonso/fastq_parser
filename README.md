Check Fastq
================================

There has been several conventions used in the quality strings of fastq files during the years.

This script takes as input a fastq file, right now unzipped but this will be changed, and reads through the lines until one can see what format is beeing used. 


Usage
-----------------------------------

*Give the path to a file to check what quality values are beeing used.(Positional argument)
*If argument --convert then the quality values are converted to sanger format, if necessary.(optional)
*If no outfile is specified the new file will have the same name as the infile but with the ending .p33.(optional)