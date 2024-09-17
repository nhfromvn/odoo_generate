from odoo import models, fields

class ResearchTitle(models.Model):
    _name = "research.title"
    _description = 'No description'


    code = fields.Char(string="Research title code", required=True)
    name = fields.Char(string="Research title name", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
