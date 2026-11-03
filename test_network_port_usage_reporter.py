import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import parse


class TestPortUsage(unittest.TestCase):
    def test_tcp_line_parsed(self):
        self.assertEqual(parse(["TCP 0.0.0.0:443 0.0.0.0:0 LISTENING"]), [(("TCP", 443), 1)])

    def test_udp_line_parsed(self):
        self.assertEqual(parse(["UDP 0.0.0.0:53 *:*"]), [(("UDP", 53), 1)])

    def test_duplicates_counted(self):
        self.assertEqual(parse(["TCP 0.0.0.0:80 x", "TCP 127.0.0.1:80 x"]), [(("TCP", 80), 2)])

    def test_junk_lines_ignored(self):
        self.assertEqual(parse(["Active Connections", ""]), [])
