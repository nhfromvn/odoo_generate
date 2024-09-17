from odoo import models, fields

class FundingAgency(models.Model):
    _name = "funding.agency"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Funding agency code", required=True)
    name = fields.Char(string="Funding agency name", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
