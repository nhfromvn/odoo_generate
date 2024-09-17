
from odoo import models, fields

class ResLang(models.Model):
    _inherit = "res.lang"
    code = fields.Char(string="Language code", required=True)
    name = fields.Char(string="Language name", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Char(string="note", required=False)
