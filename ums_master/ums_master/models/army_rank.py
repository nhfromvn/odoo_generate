from odoo import models, fields

class ArmyRank(models.Model):
    _name = "army.rank"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Army rank code", required=True)
    name = fields.Char(string="Army rank name", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
