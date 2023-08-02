# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Landed Cost Extension",
    "version": "14.0.2.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_stock",
        "stock_landed_costs",
        "ssi_product_line_account_mixin",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "views/landed_cost_type_views.xml",
        "views/stock_landed_cost_views.xml",
    ],
    "demo": [],
}
