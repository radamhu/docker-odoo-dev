# -*- coding: utf-8 -*-
{
    'name': "om_odoo_inheritance",
    'summary': "Demo: extend sale.order",
    'version': '15.0.1.0.0',
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_view.xml', # Add the XML file to the data list
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
