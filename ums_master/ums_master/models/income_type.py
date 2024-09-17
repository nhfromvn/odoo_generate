from odoo import models, fields

class IncomeType(models.Model):
    _name = "income.type"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Name ", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Code", required=True)
    type = fields.Selection(string="Type of income", required=False, selection=[('tax', 'Có thuế'), ('notax', 'Không có thuế')])
    note = fields.Text(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
