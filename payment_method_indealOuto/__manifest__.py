# Copyright 2015 Carlos Sánchez Cifuentes <csanchez@grupovermon.com>
# 
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Payment Method InDealss",
    "version": "15.0",
    "category": "",
    "author": "",
    "website": "",
    "license": "AGPL-3",
    "depends": ["sale_stock", "account", "sale_management"],
    "demo": [],
    "data": [
        "security/ir.model.access.csv",
        # "security/security.xml",
        "views/account_move_views.xml",
        "views/res_partner_view.xml",
        "views/sale_order_type_view.xml",

        
    ],
    "installable": True,
}
