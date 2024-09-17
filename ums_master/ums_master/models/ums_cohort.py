from odoo import models, fields

class UmsCohort(models.Model):
    _name = "ums.cohort"
    _description = 'No description'


    code = fields.Char(string="Course code", required=True)
    name = fields.Char(string="Course name", required=True)
    sequence = fields.Integer(string="Sequence", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
