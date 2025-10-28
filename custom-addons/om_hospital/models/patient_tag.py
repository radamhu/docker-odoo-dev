from odoo import api, fields, models, _

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string='Tag Name', required=True)
    active = fields.Boolean(string='Active', default=True, copy=False)
    color = fields.Integer(string='Color Index', default=0)
    color_hex = fields.Char(string='Color Hex')
    sequence = fields.Integer(string='Sequence')
    
    @api.returns('self', lambda value: value.id)
    # summary: Override the copy method to customize duplication behavior, 
    # ensuring the new tag has a modified name and reset sequence.
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            # default['name'] = self.name + " (copy)"
            # this is the python way of doing string formatting like above line
            default['name'] = _("%s (copy)", self.name)
        default['sequence'] = 10
        return super(PatientTag, self).copy(default)
    
    _sql_constraints = [
        ('unique_tag_name', 'unique(name, active)', 'The tag name must be unique.'),
        ('check_sequence', 'CHECK(sequence >= 0)', 'The sequence must be a non-negative integer.'),
    ]

    