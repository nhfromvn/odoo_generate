from odoo import models, fields

class ResDistrictWard(models.Model):
    _name = "res.district.ward"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Code of ward", required=True)
    name = fields.Char(string="Name of ward", required=True)
    abbr_name = fields.Char(string="Abbr Name", required=False)
    new_ward_name = fields.Char(string="New name", required=False)
    code_ward_bhxh = fields.Char(string="Code of social insurance", required=False)
    note = fields.Text(string="Note", required=False)
    district_id = fields.Many2one(string="District", comodel_name="res.state.district", required=True)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
