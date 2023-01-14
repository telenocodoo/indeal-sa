# -*- coding: utf-8 -*-

{
    'name': 'Journal Entries Approver',
    'version': '15.0.1.0',
    'description': """
    """,
    'category': 'Accounting/Accounting',
    'license': 'OPL-1',
    'depends': ['base', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/account_move.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'sequence': 1,
    'installable': True,
    'application': True,
}
