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
    ref = fields.Char(string='Reference', help='Reference for the appointment from patient record') # Reference field
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
    doctor_id = fields.Many2one("res.users", string="Doctor", tracking=True) # Many2one to res.users for doctor
    # one2many endings in _ids and many2one endings in _id
    # from hospital.appointment.pharmacy.lines import appointment_id
    pharmacy_line_ids = fields.One2many("hospital.appointment.pharmacy.lines", "appointment_id", string="Pharmacy Lines") # One2many to pharmacy lines model
    hide_sales_price = fields.Boolean(string="Hide Sale Price") # Boolean field to hide sale price

    @api.onchange('patient_id') # Onchange method to update ref when patient changes
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref
    
    def action_test(self): # Method to change state to 'in_consultation'
        print("Test button clicked")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Test button clicked',
                'type': 'rainbow_man'
            }
        }
    
    # In this model, each function is used to update the appointment's state (e.g., to 'done', 'cancel', etc.) or to react to changes in the patient selection (updating the reference field).
    def action_in_consultation(self): # Method to change state to 'in_consultation':
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self): # Method to change state to 'done':
        for rec in self:
            rec.state = 'done'
    
    def action_cancel(self): # Method to change state to 'cancel':
        action = self.env.ref('om_hospital.action_cancel_appointment_wizard').read()[0]
        return action
    
    def action_draft(self): # Method to change state to 'draft':
        for rec in self:
            rec.state = 'draft'

# define a new model for appointment pharmacy lines
# many2one to product.product for product
class AppointmentPharmacyLines(models.Model):
    _name = "hospital.appointment.pharmacy.lines" # Model name
    _description = "Appointment Pharmacy Lines" # Model description

    product_id = fields.Many2one("product.product", string="Product", required=True) # Many2one to product.product for product
    price_unit = fields.Float(related="product_id.list_price", string="Unit Price", readonly=True) # Related field to product's list price
    qty = fields.Integer(string="Quantity", default=1) # Integer field for quantity with default value
    # define many2one to hospital.appointment for appointment
    # one2many fields you should have the many2one field in the related model
    appointment_id = fields.Many2one("hospital.appointment", string="Appointment") # Many2one to hospital.appointment for appointment