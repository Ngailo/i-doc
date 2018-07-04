# -*- coding: utf-8 -*-
{
    'name': "DMS",

    'summary': """
        Saving Document""",

    'description': """
        Manage Document
    """,

    'author': "Invention Technologies",
    'website': "http://www.it.co.tz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'document',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/doc.xml',
        'views/doc_menu.xml',
        'views/doc_kanban.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}