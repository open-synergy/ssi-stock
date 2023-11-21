import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-stock",
    description="Meta package for open-synergy-ssi-stock Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_landed_cost',
        'odoo14-addon-ssi_mrp_landed_cost',
        'odoo14-addon-ssi_production_lot_qrcode',
        'odoo14-addon-ssi_stock',
        'odoo14-addon-ssi_stock_account',
        'odoo14-addon-ssi_stock_donation_operation',
        'odoo14-addon-ssi_stock_fixed_asset',
        'odoo14-addon-ssi_stock_rent_operation',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
