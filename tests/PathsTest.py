# -*- coding: utf-8 -*-
import os
import unittest
CURRENT_PATH = os.path.dirname(os.path.dirname(__file__))


class PathsTest(unittest.TestCase):
    """ Tests for checking paths """
    base_dir = CURRENT_PATH
    target_dir = None

    def check_dir(self):
        """ Method checks dirpath and create dir if not exists. """
        if not os.path.isdir(self.target_dir):
            os.mkdir(self.target_dir)
            print "Path %s successfully created!" % self.target_dir
            return True
        print "Path %s already exists!" % self.target_dir

    def test_base_dir(self):
        """ Check base files dir """
        self.target_dir = os.path.join(self.base_dir, "files")
        self.check_dir()

    def test_xml_dir(self):
        """ Check xml files dir. """
        self.target_dir = os.path.join(self.base_dir, "files/xml")
        self.check_dir()

    def test_xsl_dir(self):
        """ Check xsl files dir """
        self.target_dir = os.path.join(self.base_dir, "files/xsl")
        self.check_dir()

    def test_xml_treatment_dir(self):
        """ Check treatment dir inside xml dir """
        self.target_dir = os.path.join(self.base_dir, "files/xml/treatment")
        self.check_dir()

    def test_xsl_treatment_dir(self):
        """ Check treatment dir inside xsl dir """
        self.target_dir = os.path.join(self.base_dir, "files/xsl/treatment")
        self.check_dir()
