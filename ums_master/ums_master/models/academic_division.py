from odoo import models, fields

class AcademicDivision(models.Model):
    _name = "academic.division"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Academic division name", required=True)
    code = fields.Char(string="Academic division code", required=True)
    abbr_name = fields.Char(string="Abbr Name", required=False)
    note = fields.Text(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
