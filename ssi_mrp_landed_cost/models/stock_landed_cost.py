# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class StockLandedCost(models.Model):
    _name = "stock.landed.cost"
    _inherit = ["stock.landed.cost"]

    total_quantity = fields.Float(
        string="Total Quantity",
        compute="_compute_total_quantity",
        store=True,
    )

    @api.depends(
        "target_model",
        "picking_ids",
        "mrp_production_ids",
    )
    def _compute_total_quantity(self):
        for record in self:
            result = 0.0
            if self.target_model == "picking":
                for picking in self.picking_ids:
                    for move in picking.move_lines:
                        result += move.quantity_done
            elif self.target_model == "manufacturing":
                for mo in self.mrp_production_ids:
                    # for move in mo.move_dest_ids:
                    #     result += move.quantity_done
                    result += mo.qty_produced
            record.total_quantity = result
