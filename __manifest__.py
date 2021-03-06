# -*- coding: utf-8 -*-
{
    'name': "pcp_acc_commission_nassag",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['pcp_sales_commission_nassag'],

    # always loaded
    'data': [
        'security/commission_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'wizard/commission_invoice_wizard.xml',
        'wizard/paid_commission_wizard.xml',
        'views/res_config_settings_views.xml',
        'views/report_invoice_sales.xml',
        'views/report_account_move.xml',
        'views/account_move.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
