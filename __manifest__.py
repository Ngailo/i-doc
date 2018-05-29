# -*- coding: utf-8 -*-
{
    'name': "Document Management System",
    'summary': "document management",
    'description': """Saving Document
    """,
    'author': "Invention Technologies",
    'website': "www.it.co.tz",
    'category': 'Document Management',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'data': [
        #'security/account_security.xml',
        #'security/ir.model.access.csv',
        #'views/webclient_templates.xml',
        'views/document_view.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}