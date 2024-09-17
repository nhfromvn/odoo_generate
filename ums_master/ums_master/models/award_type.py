from odoo import models, fields

class AwardType(models.Model):
    _name = "award.type"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Name ", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Code", required=True)
    sequence = fields.Integer(string="Sequence", required=False)
    object = fields.Selection(string="Object", required=False, selection=[('gv_cbnv', 'Giảng viên/CBNV'), ('sv', 'Sinh viên')])
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
