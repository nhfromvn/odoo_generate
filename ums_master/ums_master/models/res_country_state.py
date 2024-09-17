from odoo import models, fields

class ResCountryState(models.Model):
    _inherit = "res.country.state"


    code = fields.Char(string="Code of state", required=True)
    name = fields.Char(string="Name of state", required=True)
    code_state_bhxh = fields.Char(string="Code of social insurance", required=False)
    name_state_bhxh = fields.Char(string="Name of social insurance", required=False)
    eng_name = fields.Char(string="English Name", required=False)
    other_name = fields.Char(string="Other Name", required=False)
    code_state_portal = fields.Char(string="Code of State Portal", required=False)
    note = fields.Text(string="Note", required=False)
    country_id = fields.Many2one(string="Country", comodel_name="res.country", required=True)
    district_ids = fields.One2many(string="Ward", inverse_name="state_id", comodel_name="res.state.district", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
