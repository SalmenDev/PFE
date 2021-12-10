# -*- coding: utf-8 -*-
{
    'name': "TopnetAgence",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/client.xml',
        'views/templates.xml',
        'views/AgentBardo.xml',
        'views/dossier.xml',
        'views/Agencecu.xml',
        'views/website.xml',
        'views/admin.xml',
        'views/coord.xml',
        'views/demab.xml',
        'views/historique.xml',
        'views/coord1.xml',
        'views/deposer.xml',
        'views/modifier.xml',
        'views/listeagent.xml',
        'views/fiche.xml',
        'views/suividossier.xml',
        'views/contactus.xml',
        'views/us.xml',
        'views/rdv.xml',
        'views/agence.xml',
        'views/consultagence.xml',
        'views/modif_agence.xml',
        'views/consultfiche.xml',
        'views/modif_fiche.xml',
        'views/modifag.xml',
        'views/coordag.xml',
        'views/listeagentbardo.xml',
        'views/coordbardo.xml',
        'views/modifb.xml',
        'views/suividossier.xml',
        'views/suivdoss.xml',
        'views/contrat.xml',
        'views/telecharger.xml',












    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
