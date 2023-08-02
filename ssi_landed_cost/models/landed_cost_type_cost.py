# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LandedCostTypeCost(models.Model):
    _name = "landed_cost_type.cost"
    _description = "Landed Cost Type - Cost"
    _abstract = False
    _inherit = [
        "mixin.product_line_account",
    ]

    type_id = fields.Many2one(
        comodel_name="landed_cost_type",
        string="# Landed Cost",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(string="Sequence", required=True, default=10)
