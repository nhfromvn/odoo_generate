from odoo import models, fields

class UmsPlace(models.Model):
    _name = "ums.place"
    _description = 'No description'


    name = fields.Char(string="Name", required=True)
    abbr_name = fields.Char(string="Abbr Name", required=False)
    code = fields.Char(string="code", required=True)
    note = fields.Text(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
