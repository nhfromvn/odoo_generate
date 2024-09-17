from odoo import models, fields

class ResCountry(models.Model):
    _inherit = "res.country"


    code = fields.Char(string="Code of country", required=True)
    name = fields.Char(string="Name of country", required=True)
    abbr_name = fields.Char(string="Abbr Name", required=False)
    note = fields.Text(string="Note", required=False)
    phone_code = fields.Char(string="Code of phone", required=False)
    state_ids = fields.One2many(string="State", inverse_name="country_id", comodel_name="res.country.state", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
