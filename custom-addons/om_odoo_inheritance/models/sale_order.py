from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed by')

    # inherit an existing method and extend it
    # in this case we extend action_confirm method from sale.order model
    # to set the confirmed_user_id field to the current user
    # when the sale order is confirmed
    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        print("Custom action_confirm method called")
        self.confirmed_user_id = self.env.user.id # set the current user as the confirmer, will give the current logged in user