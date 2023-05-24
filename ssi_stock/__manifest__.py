# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Inventory",
    "version": "14.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_master_data_mixin",
        "ssi_product",
        "stock",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "data/location_type_data.xml",
        "data/stock_picking_type_category_data.xml",
        "menu.xml",
        "wizards/mass_create_location_views.xml",
        "wizards/mass_create_picking_type_views.xml",
        "views/picking_type_category_views.xml",
        "views/stock_picking_type_views.xml",
        "views/stock_picking_views.xml",
        "views/location_type_views.xml",
        "views/stock_location_views.xml",
    ],
    "demo": [],
}
