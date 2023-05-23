# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ["stock.picking"]

    picking_type_category_id = fields.Many2one(
        string="Picking Type Category",
        related="picking_type_id.category_id",
        store=True,
    )
    show_price_unit = fields.Boolean(
        string="Show Price Unit",
        related="picking_type_id.show_price_unit",
        store=False,
    )
    show_procure_method = fields.Boolean(
        string="Show Procure Method",
        related="picking_type_id.show_procure_method",
        store=False,
    )
    allowed_source_location_ids = fields.Many2many(
        string="Allowed Source Locations",
        comodel_name="stock.location",
        related="picking_type_id.allowed_source_location_ids",
        store=False,
    )
    allowed_destination_location_ids = fields.Many2many(
        string="Allowed Destination Locations",
        comodel_name="stock.location",
        related="picking_type_id.allowed_destination_location_ids",
        store=False,
    )
