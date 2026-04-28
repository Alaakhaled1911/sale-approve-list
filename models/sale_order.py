from odoo import models,fields


class SalesOrder (models.Model):
    _inherit = "sale.order"


    def action_confirm(self):
        return super().action_confirm()

    def action_cancel(self):
        return super().action_cancel()



