# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = [
        "stock.picking",
        "mixin.single_operating_unit",
    ]

    @api.onchange(
        "picking_type_id",
    )
    def onchange_operating_unit_id(self):
        if self.picking_type_id and self.picking_type_id.operating_unit_id:
            self.operating_unit_id = self.picking_type_id.operating_unit_id.id
