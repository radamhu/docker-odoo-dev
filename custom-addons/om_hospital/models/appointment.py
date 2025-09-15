# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment" # Model name
    _inherit = ['mail.thread', 'mail.activity.mixin'] # To add chatter functionality
    _description = "Hospital Appointment" # Model description
    
    # Define fields many2one to link to patient model
    patient_id = fields.Many2one(
        comodel_name="hospital.patient", # Related model
        string="Patient", # Field label
    )
