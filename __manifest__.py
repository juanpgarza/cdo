# -*- coding: utf-8 -*-
{
    'name': "cdo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','hr','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cdo_menu_views.xml',
        'views/cdo_views.xml',
        'views/cdo_alta_views.xml',
        'views/cdo_rh_views.xml',
        'views/hr_menu_views.xml',
        'views/res_partner.xml',
        'views/purchase.xml',
        'reports/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}