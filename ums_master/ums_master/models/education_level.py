from odoo import models, fields

class EducationLevel(models.Model):
    _name = "education.level"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Education level code", required=True)
    name = fields.Char(string="Education level name", required=True)
    note = fields.Text(string="note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
