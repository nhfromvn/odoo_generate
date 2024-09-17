# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Job(models.Model):
    _inherit = "hr.job"
    _order = 'create_date desc'

    coefficient = fields.Float("Coefficient")
    check_create_recruitment = fields.Boolean('Created recruitment request')
    is_manager = fields.Boolean("Is Manager")
    _sql_constraints = [('job_code_unique', 'UNIQUE(job_code)', 'Vị trí công việc không được trùng!')]
    type = fields.Selection([
        ('government', 'Government'),
        ('party', 'Party'),
        ('youth_union', 'Youth Union'),
        ('trade_union', 'Trade Union'),
    ], string="Position")
    @api.model
    def create(self, vals):
        vals['job_code'] = self.env['ir.sequence'].next_by_code('job.code.sequence')
        return super(Job, self).create(vals)

        # recruitment_proposal_ids = fields.One2many('bms.hr.recruitment.proposal.detail', 'position',
        #                                            string='Đề xuất tuyển dụng')
        # number_of_recruited = fields.Integer(compute='_compute_number_of_recruited', string='Số lượng cần tuyển')

