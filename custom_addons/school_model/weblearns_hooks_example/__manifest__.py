# -*- coding: utf-8 -*-
{
    'name': "Hooks Examples",

    'summary': """
        Odoo Provides 4 Type of hooks here is the exampls.""",

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
    'depends': ['contacts'],

    # always loaded
    'data': [
        
    ],
    'pre_init_hook' :'_mycompany_pre_init_hook',
    'post_init_hook' :'_mycompany_post_init_hook',
    'uninstall_hook' :'_mycompany_uninstall_hook',
    'post_load_hook' :'_weblearns_post_load_hook',
}
