# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class StockLandedCost(models.Model):
    _name = "stock.landed.cost"
    _inherit = ["stock.landed.cost"]

    type_id = fields.Many2one(
        string="Type",
        comodel_name="landed_cost_type",
    )
    total_quantity = fields.Float(
        string="Total Quantity",
        compute="_compute_total_quantity",
        store=True,
    )

    @api.depends(
        "picking_ids",
    )
    def _compute_total_quantity(self):
        for record in self:
            result = 0.0
            for picking in self.picking_ids:
                for move in picking.move_lines:
                    result += move.quantity_done
            record.total_quantity = result

    def action_reload_cost(self):
        for record in self.sudo():
            record._reload_cost()

    def _reload_cost(self):
        self.ensure_one()
        Cost = self.env["stock.landed.cost.lines"]
        self.cost_lines.unlink()
        if self.type_id:
            for cost in self.type_id.cost_ids:
                data = {
                    "cost_id": self.id,
                    "name": cost.name,
                    "product_id": cost.product_id.id,
                    "price_unit": cost.price_subtotal * self.total_quantity,
                    "account_id": cost.account_id.id,
                    "split_method": "by_quantity",
                }
                Cost.create(data)
