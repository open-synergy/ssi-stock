# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestDropshipOperation(YamlTransactionCase):
    """Scenario tests for the Dropship picking type category setup."""

    def test_dropship_operation(self):
        """Run the master data and post-init-hook scenarios."""
        self.run_yaml_scenario("test_data_dropship_operation.yaml")

    def test_check_group_grants_edit_for_dropship_user(self):
        """Assert ``check_group`` returns ``True`` for a Dropship User.

        Pure Python — trigger P1 (L-01: ``check_group`` is a plain method
        whose boolean return value is what is under test, not a side
        effect on a record; ``action: call`` in YAML discards return
        values entirely).
        """
        category = self.env.ref("ssi_stock_dropship_operation.picking_category_ds")
        group = self.env.ref("ssi_stock_dropship_operation.dropship_user_group")
        user = self.env["res.users"].create(
            {
                "name": "Dropship User Test",
                "login": "dropship_user_test@example.com",
                "groups_id": [
                    (4, self.env.ref("base.group_user").id),
                    (4, group.id),
                ],
            }
        )
        picking_type = self.env["stock.picking.type"].search(
            [
                ("default_location_src_id.usage", "=", "supplier"),
                ("default_location_dest_id.usage", "=", "customer"),
            ],
            limit=1,
        )
        picking = self.env["stock.picking"].create(
            {
                "picking_type_id": picking_type.id,
                "location_id": self.env.ref("stock.stock_location_suppliers").id,
                "location_dest_id": self.env.ref("stock.stock_location_customers").id,
            }
        )
        self.assertTrue(
            picking.with_user(user).check_group(category.module_categ_id.id)
        )

    def test_check_group_denies_edit_for_unrelated_user(self):
        """Assert ``check_group`` returns ``False`` without the group.

        Pure Python — trigger P1 (L-01: same as above, boolean return
        value of a plain method, no record side effect to assert in YAML).
        """
        category = self.env.ref("ssi_stock_dropship_operation.picking_category_ds")
        user = self.env["res.users"].create(
            {
                "name": "Unrelated User Test",
                "login": "unrelated_user_test@example.com",
                "groups_id": [(4, self.env.ref("base.group_user").id)],
            }
        )
        picking_type = self.env["stock.picking.type"].search(
            [
                ("default_location_src_id.usage", "=", "supplier"),
                ("default_location_dest_id.usage", "=", "customer"),
            ],
            limit=1,
        )
        picking = self.env["stock.picking"].create(
            {
                "picking_type_id": picking_type.id,
                "location_id": self.env.ref("stock.stock_location_suppliers").id,
                "location_dest_id": self.env.ref("stock.stock_location_customers").id,
            }
        )
        self.assertFalse(
            picking.with_user(user).check_group(category.module_categ_id.id)
        )
