from odoo import models, fields

class TeacherTitle(models.Model):
    _name = "teacher.title"
    _description = 'No description'


    name = fields.Char(string="Title name", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Title code", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
