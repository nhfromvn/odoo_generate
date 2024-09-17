from odoo import models, fields

class CommendationMethod(models.Model):
    _name = "commendation.method"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Method name", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Method code", required=True)
    note = fields.Text(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)
    object = fields.Selection(string="Object", required=False, selection=[('gv_cbnv', 'Giảng viên/CBNV'), ('sv', 'Sinh viên')])

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
