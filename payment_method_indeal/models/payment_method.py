# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PaymentMethod(models.Model):
    _name = "payment.method"
    _description = "Payment Method"
    _check_company_auto = True


    name = fields.Char(required=True)
    # name = fields.Char(required=True, translate=True)

    account_id = fields.Many2one(
        comodel_name="account.account",
        string="Account")
    presentage_indeal = fields.Float(string="presentage % ")
