# -*- coding: utf-8 -*-
{
    'name': "Qweb Report Demo",

    'summary': """
        Qweb Report Demo""",

    'description': """
        Qweb Report Demo
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['school', 'school_student'],

    # always loaded
    'data': [
        'report/student_report_template.xml'
    ]
}
