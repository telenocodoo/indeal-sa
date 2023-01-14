# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright 2020 Tecnativa - Pedro M. Baeza

from datetime import datetime, timedelta

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    duration_indeal = fields.Integer('Duration')
    payment_method_indeal = fields.Selection([
        ('mada', 'MADA'),
        ('mastercard', 'Master Card')], string='Payment Method')
    invoice_date_indeal = fields.Date(string='Invoice Date')

   