#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2009 Tim Wintle
# SPDX-FileCopyrightText: 2015 Stéphane Galland <galland@arakhne.org>
# SPDX-FileCopyrightText: 2023 Robin Vobruba <hoijui.quaero@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause

class FileInfo(object):
    """Stores information about the version of a graffle document"""
    def __init__(self, gdict):
        """Grab all file info from this dict"""
        self.fmt_version = int(gdict.get("GraphDocumentVersion",-1))
        self.creator = gdict.get("Creator","")
        self.creationdate = gdict.get("CreationDate","")
        self.app_version = gdict.get("ApplicationVersion",[])
        self.modified = gdict.get("ModificationDate","")
        self.printinfo = PrintInfo(gdict.get("PrintInfo",{}))

class PrintInfo(object):
    """Gets the Print information from the file's dict
       - possible confusion over the formatting, so store separately."""
    def __init__(self, pinfo):
        self._print_info = pinfo

    bottom_margin = property(fget = lambda x: x.extract_value("NSBottomMargin",0))
    left_margin = property(fget = lambda x: x.extract_value("NSLeftMargin",0))
    right_margin = property(fget = lambda x: x.extract_value("NSRightMargin",0))
    top_margin = property(fget = lambda x: x.extract_value("NSTopMargin",0))
    orientation = property(fget = lambda x: x.extract_value("NSOrientation",1))
    paper_name = property(fget = lambda x: x.extract_value("NSPaperName",""))
    paper_size = property(fget = lambda x: x.extract_value("NSPaperSize",[100,100]))

    def extract_value(self, key, default):
        """input format is similar to:
        {key:[type, value]}
        """
        somelist = self._print_info.get(key)
        if somelist is None:
            return default
        typ = somelist[0]
        if typ == "int":
            return int(somelist[1])
        elif typ == "size":
            # e.g. {12,32}
            valueparts = somelist[1][1:-1].split(",")
            return [float(a) for a in valueparts]
        elif typ == "coded":
            pass
            #raise NotImplementedError("'Coded' type not implemented")
        return default
