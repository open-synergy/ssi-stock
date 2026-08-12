# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestDropshipApproval(YamlTransactionCase):
    """Scenario tests for Dropship approver resolution.

    Kept in its own file/method (test-traps T-01): the scenario writes
    ``manager_id`` on the shared Dropship category record, so it is
    isolated from :mod:`test_dropship_operation` to avoid leaking state
    across scenarios that share the same DB transaction.
    """

    def test_dropship_approval(self):
        """Run the approver-resolution scenario for Dropship pickings."""
        self.run_yaml_scenario("test_data_dropship_approval.yaml")
