# -*- coding: utf-8 -*-
from datetime import date

from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient" # Model name
    _inherit = ['mail.thread', 'mail.activity.mixin'] # To add chatter functionality
    _description = "Hospital Patient" # Model description

    name = fields.Char(string='Patient Name', tracking=True) # Patient Name. breadcrumbs will show patient name
    date_of_birth = fields.Date(string='Date of Birth') # Date of Birth
    ref = fields.Char(string='Reference') # Reference
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True, store=True) # Computed field for Age
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True, tracking=True, default='female')
    active = fields.Boolean(string='Active', default=True, tracking=True) # Active / action archived button
    appointment_id = fields.Many2one( # One2many field to link to appointments model
        "hospital.appointment", # Related model
        string="Appointments" # Field label
    )

    """
    Compute the age of the patient based on their date of birth.
    This method calculates the patient's age by comparing the current date
    with the patient's date_of_birth. If the date_of_birth is not set, the age
    is set to 0.
    The computed age is stored in the 'age' field for each record.
    Returns:
        None
    """
    @api.depends('date_of_birth') # lively update when date_of_birth changes
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0