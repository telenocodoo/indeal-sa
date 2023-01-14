# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_cr_indeal = fields.Char('Company Registry')
    legal_name_in_english_indeal = fields.Char('Legal by Company')
