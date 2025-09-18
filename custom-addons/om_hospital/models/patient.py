# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient" # Model name
    _inherit = ['mail.thread', 'mail.activity.mixin'] # To add chatter functionality
    _description = "Hospital Patient" # Model description

    name = fields.Char(string='Patient Name', required=True, tracking=True) # Patient Name
    ref = fields.Char(string='Reference', required=True, tracking=True, default='New') # Reference
    age = fields.Integer(string='Age', required=True, tracking=True) # Age
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True, tracking=True, default='female')
    active = fields.Boolean(string='Active', default=True, tracking=True) # Active / action archived button
    # medical_history = fields.Text(string='Medical History')
    # type = fields.Selection([
    #     ('other', 'Regular'),
    #     ('receivable', 'Receivable'),
    #     ('payable', 'Payable'),
    #     ('liquidity', 'Liquidity'),
    # ], required=True, default='other',
    #     help="The 'Internal Type' is used for features available on "\
    #     "different types of accounts: liquidity type is for cash or bank accounts"\
    #     ", payable/receivable is for vendor/customer accounts.")