# -*- coding: utf-8 -*-

import os
import unittest
CURRENT_PATH = os.path.dirname(os.path.dirname(__file__))
XML_DIR = "files/xml"
XSL_DIR = "files/xsl"


class XmlFilesTest(unittest.TestCase):

    xmlfile_path = None

    def test_if_treatment_dir_exists(self):
        self.xmlfile_path = os.path.join(CURRENT_PATH, XML_DIR, "treatment")
        if os.path.isdir(self.xmlfile_path):
            print "Path for treatment files %s exists. " % self.xmlfile_path,
        else:
            print "Path %s was not found." % self.xmlfile_path,

    def test_import_lxml(self):
        try:
            import lxml
            print "%s module successfully imported. " % lxml.__name__
        except ImportError:
            print """
            Lxml import failed. Consider install LXML module via pip
            or easy_install into your current virtual environment.
            """

    def test_files_in_xml_dir(self):
        self.xmlfile_path = os.path.join(CURRENT_PATH, XML_DIR, "treatment")
        print "%d files in path %s found. " % \
            (len(os.listdir(self.xmlfile_path)), self.xmlfile_path)
    
    """
    def test_xml_file_parsing(self):
        self.xmlfile_path = os.path.join(CURRENT_PATH, XML_DIR, "treatment")
        self.xslfile_path = os.path.join(CURRENT_PATH, XSL_DIR, "treatment")
        xmlfiles = os.listdir(self.xmlfile_path)
        xslfiles = os.listdir(self.xslfile_path)
        if xmlfiles:
            res = []
            from lxml import etree
            xml_file = etree.parse(os.path.join(self.xmlfile_path, xmlfiles[0]))
            if xslfiles:
                xslt_file = etree.parse(os.path.join(self.xslfile_path, xslfiles[0]))
                transform = etree.XSLT(xslt_file)
                res = transform(xml_file)
            print res
        return True
    """
