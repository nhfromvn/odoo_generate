from odoo import models, fields

class DecisionType(models.Model):
    _name = "decision.type"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Name ", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Code", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
