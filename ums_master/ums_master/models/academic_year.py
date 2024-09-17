from odoo import models, fields

class AcademicYear(models.Model):
    _name = "academic.year"
    _description = 'No description'


    code = fields.Char(string="Academic year code", required=True)
    name = fields.Char(string="Academic year name", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
