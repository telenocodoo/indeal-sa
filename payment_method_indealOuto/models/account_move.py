# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright 2020 Tecnativa - Pedro M. Baeza

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    duration_indeal = fields.Integer('Duration')
    payment_method_indeal = fields.Many2one(
        comodel_name="payment.method",
        string="Payment Method",
        store=True,
        copy=True,
    )
    logistic_inv_indeal = fields.Boolean(string="Logistic Invoice",default=False)
    invoice_date_indeal = fields.Date(string='Invoice Date')
    shipment_id_ideal = fields.Date(string='Shipment ID')
    buyer_indeal = fields.Many2one( comodel_name="res.company",string='Buyer' )

