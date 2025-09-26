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
        # 'data/admin_sales_rights.xml', # Initial data for admin sales rights
        'data/patient_tag_data.xml', # Initial data for patient tags
        'data/patient.tag.csv', # Initial data for patient tags
        'wizard/cancel_appointment_view.xml', # Wizard views order is important here transient models first after security
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
