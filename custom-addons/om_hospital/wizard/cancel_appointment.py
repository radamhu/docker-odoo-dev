from odoo import models, fields, api

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment', required=True)
    reason = fields.Text(string='Reason for Cancellation')
    
    def action_cancel(self):
        return