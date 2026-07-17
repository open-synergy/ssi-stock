# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Valuation Layer Usage Recomputation + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_stock_valuation_layer_recomputation",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/svl_recomputation.xml",
        "security/ir_rule/svl_recomputation.xml",
        "view/svl_recomputation.xml",
    ],
}
