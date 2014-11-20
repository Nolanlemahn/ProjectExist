#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013 Paulo Scardine
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#-------------------------------------------------------------------------------
# Name:        get_image_size
# Purpose:     extract image dimentions given a file path
#
# Author:      Paulo Scardine (based on code from Emmanuel VAÏSSE)
#
# Created:     26/09/2013
# Copyright:   (c) Paulo Scardine 2013
# Licence:     MIT
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import os
import struct

FILE_UNKNOWN = "Sorry, don't know how to get size for this file."
BROKEN_FILE = "Sorry, I have no idea where that was."

class BadFile(Exception):
    pass

class UnknownImageFormat(Exception):
    pass

def get_image_size(file_path):
    """
    Return (width, height) for a given img file content - no external
    dependencies except the os and struct builtin modules
    """
    if(not os.path.isfile(file_path)):
        raise BadFile(BROKEN_FILE)
    size = os.path.getsize(file_path)
    
    with open(file_path, "rb") as input:
        height = -1
        width = -1
        data = input.read(25)
        msg = " raised while trying to decode as JPEG."

        if (size >= 10) and data[:6] in ('GIF87a', 'GIF89a'):
            # GIFs
            w, h = struct.unpack("<HH", data[6:10])
            width = int(w)
            height = int(h)
        elif ((size >= 24) and data.startswith('\211PNG\r\n\032\n')
              and (data[12:16] == 'IHDR')):
            # PNGs
            w, h = struct.unpack(">LL", data[16:24])
            width = int(w)
            height = int(h)
        elif (size >= 16) and data.startswith('\211PNG\r\n\032\n'):
            # older PNGs
            w, h = struct.unpack(">LL", data[8:16])
            width = int(w)
            height = int(h)
        elif (size >= 2) and data.startswith('\377\330'):
            # JPEG
            input.seek(0)
            input.read(2)
            b = input.read(1)
            try:
                while (b and ord(b) != 0xDA):
                    while (ord(b) != 0xFF): b = input.read(1)
                    while (ord(b) == 0xFF): b = input.read(1)
                    if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                        input.read(3)
                        h, w = struct.unpack(">HH", input.read(4))
                        break
                    else:
                        input.read(int(struct.unpack(">H", input.read(2))[0])-2)
                    b = input.read(1)
                width = int(w)
                height = int(h)
            except struct.error:
                raise UnknownImageFormat("StructError" + msg)
            except ValueError:
                raise UnknownImageFormat("ValueError" + msg)
            except Exception as e:
                raise UnknownImageFormat(e.__class__.__name__ + msg)
        elif size >= 2:
        	#see http://en.wikipedia.org/wiki/ICO_(file_format)
        	input.seek(0)
        	reserved = input.read(2)
        	if 0 != struct.unpack("<H", reserved )[0]:
        		raise UnknownImageFormat(FILE_UNKNOWN)
        	format = input.read(2)
        	assert 1 == struct.unpack("<H", format)[0]
        	num = input.read(2)
        	num = struct.unpack("<H", num)[0]
        	if num > 1:
        		import warnings
        		warnings.warn("ICO File contains more than one image")
        	#http://msdn.microsoft.com/en-us/library/ms997538.aspx
        	w = input.read(1)
        	h = input.read(1)
        	width = ord(w)
        	height = ord(h)
        else:
            raise UnknownImageFormat(FILE_UNKNOWN)

    return width, height

