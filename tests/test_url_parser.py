import unittest

from lib.url_parser import LinkedInURLValidationError, parse_linkedin_url


class UrlParserTests(unittest.TestCase):
    def test_accepts_supported_https_linkedin_urls_only(self):
        parsed = parse_linkedin_url("https://www.linkedin.com/posts/example")
        self.assertEqual(parsed.canonical, "https://www.linkedin.com/posts/example")
        with self.assertRaises(LinkedInURLValidationError):
            parse_linkedin_url("http://www.linkedin.com/posts/example")
        with self.assertRaises(LinkedInURLValidationError):
            parse_linkedin_url("https://linkedin.com.evil.example/posts")
