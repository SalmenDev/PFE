# -*- coding: utf-8 -*-
{
    'name': "Topnet",

    'summary': """
        Topnet Customer Manager Platform""",

    'description': """
        Platefrome de gestion des dossiers clients TOPNET
    """,

    'author': "Topnet, Salmen Aouini",
    'website': "https://www.topnet.tn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/adduser.xml',
        'views/add_FO.xml',
        'views/add_contact.xml',
        'data/ir_config_parameter.xml',
        'templates/website_templates.xml',
        'templates/webclient_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'views/user.xml',
    ],
    'installable':True,
    'application' : True, 
    'auto_install' : False,
    'sequence':'10', 
    'images': ['static/description/banner.png'],
}
