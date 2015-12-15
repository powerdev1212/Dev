# -*- coding: utf-8 -*-
import platform
import unittest


class PlatformTest(unittest.TestCase):

    def test_node_for_current_system(self):
        
        print platform.node()
