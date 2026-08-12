# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    """Link the native Dropship picking type to this module's category.

    ``stock_dropshipping`` auto-creates its operation type without an
    XML ID, so it cannot be referenced with ``env.ref()``. This finds
    it with the same domain Odoo core itself uses
    (``default_location_src_id.usage=supplier``,
    ``default_location_dest_id.usage=customer``) and sets its
    ``category_id`` to the ``picking_type_category`` this module ships.

    :param cr: database cursor active during module installation
    :param registry: Odoo registry being loaded
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    picking_type = env["stock.picking.type"].search(
        [
            ("default_location_src_id.usage", "=", "supplier"),
            ("default_location_dest_id.usage", "=", "customer"),
        ]
    )
    category = env.ref(
        "ssi_stock_dropship_operation.picking_category_ds", raise_if_not_found=False
    )
    if picking_type and category:
        picking_type.write({"category_id": category.id})
