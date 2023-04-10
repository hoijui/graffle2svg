#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2009 Tim Wintle
# SPDX-FileCopyrightText: 2011 Jean-Noel Avila <jn.avila@free.fr>
# SPDX-FileCopyrightText: 2015 Stéphane Galland <galland@arakhne.org>
# SPDX-FileCopyrightText: 2020 Jean-Noël Avila <jn.avila@free.fr>
# SPDX-FileCopyrightText: 2023 Robin Vobruba <hoijui.quaero@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause

import gzip
from urllib.request import urlopen
import chardet

class GraffleFilePack(object):
	__file = None

	def __init__(self,fn):
		if not fn:
			raise Exception("You must specify an input file")
		elif self.detectGZipXMLFile(fn):
			self.__file = gzip.open(fn, "rb")
		elif self.detectXMLFile(fn):
			self.__file = open(fn,"rb")
		else:
			raise Exception("Invalid input file: %s" % (fn))

	@property
	def fileObject(self):
		return self.__file

	def read(self):
		return self.__file.read()

	def close(self):
		self.__file.close()

	def detectGZipXMLFile(self,fn):
		"""Is this a zipped xml file"""
		result = False
		try:
			f = gzip.open(fn, 'rb')
			try:
				byteString = f.readline()
				result = (byteString and byteString[:5] == b'<?xml')
			except:
				result = False
			f.close()
		except:
			pass
		return result

	def detectXMLFile(self,fn):
		"""Is this an xml file"""
		result = False
		encoding = self.__detectEncoding(fn)
		if encoding and encoding['encoding']:
			encoding = encoding['encoding']
			try:
				f = open(fn, "r", encoding=encoding)
				try:
					string = f.readline()
					result = (string and string[:5] == '<?xml')
				except:
					result = False
				f.close()
			except:
				pass
		return result

	def __detectEncoding(self, fn):
		fh = urlopen("file:%s" % (fn))
		result = chardet.detect(fh.read())
		fh.close()
		return result

if __name__ == "__main__":
    gfp = GraffleFilePack("gziptest.graffle")
    print(gfp.read())
