#!/usr/bin/python
'''
Usage: passwordGenerator.py [-h] [-v] [-l LENGTH] [-o OUTPUT] [-c CHARSET]

Python password generator

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Enable verbose output
  -l LENGTH, --length LENGTH Length of the password
  -o OUTPUT, --output OUTPUT Saves the result in a file
  -c CHARSET, --charset CHARSET Characters to iterate
'''

import sys
import time
import random
import logging
import argparse

def createPassword(chars, length, output):
	logging.info('[I] Starting time: %s' % time.strftime('%H:%M:%S'))
	result = ''.join(random.choice(chars) for _ in range(length))
	logging.debug('[D] Result : %s' % result)

	logging.debug('[D] Openning result file')
	output = open(output, 'w')
	logging.debug('[D] Writing %s in result file' % result)
	output.write(result + '\n')
	logging.debug('[D] Closing result file')
	output.close()

	logging.info('[I] End time: %s' % time.strftime('%H:%M:%S'))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='Python password generator')
	parser.add_argument('-v', '--verbose',    action='store_true', help='Enable verbose output',                             default=False)
	parser.add_argument('-l', '--length',     type=int,            help='Length of the password',                            default=16)
	parser.add_argument('-o', '--output',                          help='Saves the result in a file',                        default='password.txt')
	parser.add_argument('-c', '--charset',                         help='Characters to iterate',                             default='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/*-+.&(_)=$!:;,#{[|@]}<>')
	if len(sys.argv) < 3:
		parser.print_help()
	args = parser.parse_args()
	level = logging.DEBUG if args.verbose else logging.INFO
	logging.basicConfig(level=level, format='[%(asctime)s.%(msecs)03d]  %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
	createPassword(args.charset, args.length, args.output)