# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Healthcare',
    'author': 'Adam informatika', # Author of the module
    'sequence': -100, # Ensures it appears early in the apps list
    'summary': 'Manage hospital operations and patient records',
    'description': """
    """,
    'depends': [], # Dependencies
    'data': [
        'security/ir.model.access.csv', # Security rules
        'views/menu.xml', # Patient views
        'views/patient_view.xml', # Doctor views
        'views/female_patient_view.xml', # Female patient views
        ], # Data files
    'demo': [], # Demo data files
    'application': True, # This is a custom application
    'auto_install': False, # This module will not be installed automatically
    'license': 'LGPL-3',
}
