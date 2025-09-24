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
    'depends': [
        'mail', # For Chatter functionality
        'product' # For product management in pharmacy lines
        ], # Dependencies
    'data': [
        'security/ir.model.access.csv', # Security rules
        'views/menu.xml', # Patient views
        'views/patient_view.xml', # Doctor views
        'views/female_patient_view.xml', # Female patient views
        'views/appointment_view.xml', # Appointment views
        'views/patient_tag_view.xml', # Patient Tag views
        ], # Data files
    'demo': [], # Demo data files
    'application': True, # This is a custom application
    'auto_install': False, # This module will not be installed automatically
    'license': 'LGPL-3',
}
