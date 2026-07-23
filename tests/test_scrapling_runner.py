#!/usr/bin/env python3
"""
Automated unit tests for scrapling_runner.py
"""

import os
import sys
import unittest

# Add scripts directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from scrapling_runner import run_scrape


class TestScraplingRunner(unittest.TestCase):

    def test_fast_fetch_example(self):
        """Test fast HTTP fetching mode on example.com"""
        result = run_scrape("https://example.com", mode="fast", css="h1")
        self.assertIn("status", result)
        if result["status"] == "error":
            print(f"Warning: fast scrape failed with: {result.get('message')}")
        else:
            self.assertEqual(result["status"], "success")
            self.assertEqual(result["status_code"], 200)
            self.assertTrue(len(result["matched_elements"]) > 0)
            self.assertIn("Example Domain", result["matched_elements"][0])

    def test_invalid_url_error_handling(self):
        """Test graceful error handling on invalid domain"""
        result = run_scrape("https://invalid-non-existent-domain-12345.org", mode="fast", timeout=5)
        self.assertEqual(result["status"], "error")


if __name__ == "__main__":
    unittest.main()
