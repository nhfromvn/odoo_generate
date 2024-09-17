from odoo import models, fields

class RevenueSource(models.Model):
    _name = "revenue.source"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Revenue Source Name", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Revenue Source Code", required=True)
    note = fields.Text(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
