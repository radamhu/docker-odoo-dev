import datetime
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    # Set default appointment based on context
    # must be placed before the field definition
    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        res['date_cancelled'] = datetime.datetime.now()
        return res

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment', required=True)
    reason = fields.Text(string='Reason for Cancellation', default='No reason provided')
    date_cancelled = fields.Datetime(string='Cancellation Date')
    
    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_('Cannot cancel an appointment on the same day.'))
        return