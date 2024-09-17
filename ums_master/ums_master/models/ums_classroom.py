from odoo import models, fields

class UmsClassroom(models.Model):
    _name = "ums.classroom"
    _description = 'No description'


    name = fields.Char(string="Name", required=True)
    abbr_name = fields.Char(string="Abbr Name", required=False)
    code = fields.Char(string="code", required=True)
    floor = fields.Char(string="Floor", required=True)
    capacity = fields.Integer(string="Capacity", required=True)
    open_state = fields.Selection(string="Open State", required=False, selection=[('open', 'Mở cửa'), ('close', 'Đóng cửa')])
    register_state = fields.Selection(string="Register State", required=False, selection=[('allow', 'Được đăng ký'), ('not_allow', 'Không được đăng ký')])
    approval_state = fields.Selection(string="Approval State", required=False, selection=[('yes', 'Cần phê duyệt'), ('no', 'Không cần phê duyệt')])
    note = fields.Text(string="Note", required=False)
    place_id = fields.Many2one(string="Place", comodel_name="ums.place", required=True)
    room_type_id = fields.Many2one(string="Room Type", comodel_name="ums.room.type", required=True)
    department_id = fields.Many2one(string="Management Department", comodel_name="hr.department", required=True)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
