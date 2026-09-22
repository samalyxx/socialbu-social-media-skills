import unittest

from lib.approval import ApprovalError, ApprovalGate, PublishAction, PublishIntent


class ApprovalTests(unittest.TestCase):
    def test_exact_current_confirmation_is_single_use(self):
        intent = PublishIntent(PublishAction.PUBLISH_NOW, "https://www.linkedin.com/in/example", "Hello LinkedIn")
        gate = ApprovalGate(token_factory=lambda: "test-token")
        request = gate.prepare(intent)
        with self.assertRaises(ApprovalError):
            gate.confirm(request, "yes")
        permit = gate.confirm(request, request.required_confirmation)
        gate.consume(permit, intent)
        with self.assertRaises(ApprovalError):
            gate.consume(permit, intent)
