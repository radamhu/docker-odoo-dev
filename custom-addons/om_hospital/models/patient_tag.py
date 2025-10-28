from odoo import api, fields, models

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string='Tag Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string='Color Index', default=0)
    color_hex = fields.Char(string='Color Hex')
    sequence = fields.Integer(string='Sequence')
    
    _sql_constraints = [
        ('unique_tag_name', 'unique(name, active)', 'The tag name must be unique.'),
        ('check_sequence', 'CHECK(sequence >= 0)', 'The sequence must be a non-negative integer.'),
    ]
