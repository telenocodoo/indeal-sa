# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class helpdesk_ticket(models.Model):
    _inherit = 'helpdesk.ticket'

    sequence_name = fields.Char("Sequence",readonly=True)
    desc_reqest = fields.Char('وصف الطلب', required=True)
    indeal_cr = fields.Char(string='CR', compute='_compute_cr_name', store=True, readonly=False)

    @api.depends('partner_id')
    def _compute_cr_name(self):
        for ticket in self:
            if ticket.partner_id:
                ticket.indeal_cr = ticket.partner_id.x_cr_indeal



    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('helpdesk.ticket') or _('New')
        res = super(helpdesk_ticket, self).create(vals)
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: