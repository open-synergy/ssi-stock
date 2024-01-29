# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Inventory",
    "version": "14.0.2.13.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_master_data_mixin",
        "ssi_product",
        "stock",
        "stock_move_backdating",
        "stock_inventory_preparation_filter",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "data/location_type_data.xml",
        "data/stock_picking_type_category_data.xml",
        "menu.xml",
        "templates/picking_type_m2_configurator_templates.xml",
        "templates/picking_type_category_m2_configurator_templates.xml",
        "wizards/mass_create_location_views.xml",
        "wizards/mass_create_picking_type_views.xml",
        "views/picking_type_category_views.xml",
        "views/stock_picking_type_views.xml",
        "views/stock_picking_views.xml",
        "views/location_type_views.xml",
        "views/product_category_views.xml",
        "views/stock_location_views.xml",
        "views/goods_receipt_views.xml",
        "views/delivery_order_views.xml",
        "views/internal_transfer_views.xml",
        "views/pick_views.xml",
        "views/pack_views.xml",
        "views/consume_views.xml",
        "views/waste_views.xml",
        "views/stolen_views.xml",
        "views/lost_views.xml",
        "views/adjustment_in_views.xml",
        "views/adjustment_out_views.xml",
        "views/interwarehouse_in_views.xml",
        "views/interwarehouse_out_views.xml",
    ],
    "demo": [],
}
