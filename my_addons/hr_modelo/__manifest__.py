# -*- coding: utf-8 -*-
{
    'name': "hr_modelo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Glezvidal",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Proceso de Selección',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_recruitment','hr_nomengladores'],

    # always loaded
    'data': [
        'security/segurity_hr_modelo.xml',
        'security/ir.model.access.csv',
        'views/hr_area.xml',
        'views/templates.xml',
        'views/hr_prempleao.xml',
        'views/hr_searchRe.xml',
        'views/hr_resumen.xml',
        'views/hr_psico.xml',
        'views/hr_evalua.xml',
        'views/hr_menu.xml'

    ],
    # only loaded in demonstration mode
    'application': True,
    'installable': True,
}
