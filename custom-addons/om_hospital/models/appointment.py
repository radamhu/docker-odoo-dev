# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment" # Model name
    _inherit = ['mail.thread', 'mail.activity.mixin'] # To add chatter functionality
    _description = "Hospital Appointment" # Model description
    _rec_name = 'patient_id' # Set the record name to the 'patient_id' field, breadcrumbs will show patient name
    
    # Define fields many2one to link to patient model
    patient_id = fields.Many2one("hospital.patient", # Related model
        string="Patient", # Field label
    )
    gender = fields.Selection(related='patient_id.gender') # Related field to patient
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now) # Datetime field with default value
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today) # Date field with default value
    ref = fields.Char(string='Reference') # Reference
    prescription = fields.Html(string="Prescription") # HTML field for rich text
    priority = fields.Selection([ # Stars widget for priority
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string="Priority", default='1') # Default priority is 'Normal'
    state = fields.Selection([ # Status widget for state
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string="State", default='draft', required=True) # Default state is 'Normal'

    @api.onchange('patient_id') # Onchange method to update ref when patient changes
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref
    
    def action_start_consultation(self): # Method to change state to 'in_consultation'
        self.state = 'in_consultation'