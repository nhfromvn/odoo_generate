from odoo import models, fields

class ScientificTitle(models.Model):
    _name = "scientific.title"
    _description = 'No description'


    code = fields.Char(string="Scientific title code", required=True)
    name = fields.Char(string="Scientific title name", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
