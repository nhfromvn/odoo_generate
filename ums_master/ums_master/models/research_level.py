from odoo import models, fields

class ResearchLevel(models.Model):
    _name = "research.level"
    _description = 'No description'


    code = fields.Char(string="Research level code", required=True)
    name = fields.Char(string="Research level name", required=True)
    note = fields.Text(string="note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
