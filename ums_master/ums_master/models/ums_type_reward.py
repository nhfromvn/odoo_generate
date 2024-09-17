from odoo import models, fields

class UmsTypeReward(models.Model):
    _name = "ums.type.reward"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name", required=True)
    note = fields.Text(string="Note", required=False)
    abbr_name = fields.Char(string="Abbrevation Name", required=False)
    sequence = fields.Integer(string="Sequence", required=False)
    object = fields.Selection(string="Object", required=False, selection=[('officer', 'Officers'), ('student', 'Students')])
    award_type_id = fields.Many2one(string="Award type", comodel_name="award.type", required=True)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
