# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestStockValuationLayerPartner(TransactionCase):
    def test_partner_id_is_readonly_without_inverse(self):
        """SVL partner_id must never write back to stock.picking.partner_id.

        A writable related field installs an inverse, so creating a SVL with
        context default_partner_id (e.g. vacuum revaluation triggered while
        validating a Goods Receipt opened from a PO) overwrote the Contact of
        an unrelated Delivery Order.
        """
        field = self.env["stock.valuation.layer"]._fields["partner_id"]
        self.assertEqual(field.related, ("stock_move_id", "picking_id", "partner_id"))
        self.assertTrue(field.readonly)
        self.assertFalse(field.inverse)
