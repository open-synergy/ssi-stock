# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class LandedCostType(models.Model):
    _name = "landed_cost_type"
    _inherit = ["mixin.master_data"]
    _description = "Landed Cost Type"

    cost_ids = fields.One2many(
        string="Costs",
        comodel_name="landed_cost_type.cost",
        inverse_name="type_id",
    )
