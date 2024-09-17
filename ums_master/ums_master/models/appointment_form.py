from odoo import models, fields

class AppointmentForm(models.Model):
    _name = "appointment.form"
    _description = 'No description'


    name = fields.Char(string="Form Name", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Form code", required=True)
    note = fields.Text(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
