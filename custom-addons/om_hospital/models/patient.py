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
    image = fields.Image(string="Patient Image") # Image field for patient photo
    tag_ids = fields.Many2many( # Many2many field for patient tags, this wont be stored in  hospital_patient table
        "patient.tag", # Related model
        string="Tags" # Field label
    )

    @api.model
    # inherit create method to add custom logic during record creation
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New' # Generate a sequence for the ref field
        return super(HospitalPatient, self).create(vals) # Call the super method to ensure the record is created

    # inherit write method to add custom logic during record update
    def write(self, vals):
        # print("Write method called with vals:", vals) # Debug print to check the values being written
        if not self.ref and not vals.get('ref'): # If ref is not set in the existing record and not being updated
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New' # Generate a sequence for the ref field if not already set
        return super(HospitalPatient, self).write(vals) # Call the super method to ensure the record is updated
    
    @api.depends('date_of_birth') # lively update when date_of_birth changes
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0