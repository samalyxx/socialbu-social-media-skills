import unittest

from lib.config import MCP_ENDPOINT, RuntimeMode, load_config


class ConfigTests(unittest.TestCase):
    def test_defaults_to_draft_only_mode(self):
        self.assertEqual(load_config({}).mode, RuntimeMode.DRAFT_ONLY)
        settings = load_config({
            "LINKEDIN_SKILLS_MODE": "connected",
            "LINKEDIN_SKILLS_MCP_ENDPOINT": MCP_ENDPOINT,
        })
        self.assertEqual(settings.mode, RuntimeMode.CONNECTED)
        self.assertFalse(settings.mutation_authorized)
