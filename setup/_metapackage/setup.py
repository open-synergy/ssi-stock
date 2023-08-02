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
        'odoo14-addon-ssi_stock',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
