from odoo import models, fields

class PaygradeLevel(models.Model):
    _name = "paygrade.level"
    _description = 'No description'


    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name", required=True)
    note = fields.Text(string="Note", required=False)
    abbr_name = fields.Char(string="Abbrevation Name", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
