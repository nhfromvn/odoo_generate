from odoo import models, fields

class ResStateDistrict(models.Model):
    _name = "res.state.district"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Code of district", required=True)
    name = fields.Char(string="Name of district", required=True)
    code_district_bhxh = fields.Char(string="Code of social insurance", required=False)
    new_district_name = fields.Char(string="New name", required=False)
    note = fields.Text(string="Note", required=False)
    state_id = fields.Many2one(string="State", comodel_name="res.country.state", required=True)
    ward_ids = fields.One2many(string="Ward", inverse_name="district_id", comodel_name="res.district.ward", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
