# -*- coding: utf-8 -*-
from odoo import api, models, fields, _


class HrAllowance1(models.Model):
    _name = "hr.allowance.1"

    name = fields.Char(string="Name")
    abbreviations = fields.Char(string="Abbreviations")
    tinh_bhxh = fields.Boolean(string="Calculate BHXH")
    note = fields.Char(string="Note")


class HrAllowance2(models.Model):
    _name = "hr.allowance.2"

    level_work_capacity_decline = fields.Char(string="Level of loss of working ability")
    minimum_compensation = fields.Char(string="Minimum compensation level")
    minimum_subsidy_level = fields.Char(string="Minimum subsidy level")
    note = fields.Char(string="Note")


class HrRewardForm(models.Model):
    _name = "hr.reward.form"
    _rec_name = 'type_reward'

    type_reward = fields.Char(string="Type")
    abbreviations = fields.Char(string="Abbreviations")
    note = fields.Char(string="Note")


class HrRewardDecision(models.Model):
    _name = "hr.reward.decision"
    name = fields.Char(string="Name ", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Code", required=True)
    object = fields.Selection(string="Object", required=True,
                              selection=[('gv_cbnv', 'Giảng viên/CBNV'), ('sv', 'Sinh viên')])
    note = fields.Char(string="Note", required=False)


class BmsHrContractType(models.Model):
    _name = "bms.hr.contract.type"

    name = fields.Char(string="Name ", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Code", required=True)
    sequence = fields.Integer(string="Sequence", required=False)
    note = fields.Char(string="Note", required=False)
    month = fields.Integer(string="Month", required=True)
    month_term = fields.Char(string="Month term")


class HrReasonArchive(models.Model):
    _name = "hr.reason.archive"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")


class HrBackground(models.Model):
    _name = "hr.background"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")


class HrEthnic(models.Model):
    _name = "hr.ethnic"
    name = fields.Char(string="Name ethnicity", required=True)
    abbr_name = fields.Char(string="Abbreviation", required="FASLE")
    code = fields.Char(string="Ethnic code", required=True)
    note = fields.Char(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)


class HrPlaceMedical(models.Model):
    _name = "hr.place.medical"

    name = fields.Char(string="Name")
    abbr_name = fields.Char(string="Abbr Name", required="FASLE")
    code = fields.Char(string="code", required=True)
    note = fields.Char(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)


class HrReligion(models.Model):
    _name = "hr.religion"
    name = fields.Char(string="Name religion", required=True)
    abbr_name = fields.Char(string="Abbreviation", required="FASLE")
    code = fields.Char(string="Religious code", required=True)
    note = fields.Char(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)


class HrHealthCondition(models.Model):
    _name = "hr.health.condition"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")


class HrFamilyRelationship(models.Model):
    _name = "hr.family.relationship"
    name = fields.Char(string="Name", required=True)
    abbr_name = fields.Char(string="Abbr Name", required="FASLE")
    code = fields.Char(string="code", required=True)
    note = fields.Char(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)


class HrFormTraining(models.Model):
    _name = "hr.form.training"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")


class HrPoliticalTheory(models.Model):
    _name = "hr.political.theory"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Level code", size=10, required=True)


class HrStateManagement(models.Model):
    _name = "hr.state.management"
    name = fields.Char(string="Qualification Title", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Level code", required=True)
    note = fields.Char(string="Note", required=False)


class HrEconomicManagement(models.Model):
    _name = "hr.economic.management"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")


class HrEnglishLevel(models.Model):
    _name = "hr.english.level"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")


class HrComputerSkill(models.Model):
    _name = "hr.computer.skill"
    name = fields.Char(string="Qualification Title", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Level code", required=True)
    note = fields.Char(string="Note", required=False)


class HrAcademicRank(models.Model):
    _name = "hr.academic.rank"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")


class HrDegree(models.Model):
    _name = "hr.degree"
    _description = 'Academic Degree'

    name = fields.Char(string="Name academic degree", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Degree code", required=True)
    note = fields.Text(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)


class HrForeignLanguage(models.Model):
    _name = "hr.foreign.language"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")


class HrAcademicLevel(models.Model):
    _name = "hr.academic.level"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Level code", required=True)
class HrMarital(models.Model):
    _name = "hr.marital"

    name = fields.Char(string="Name")
    note = fields.Char(string="Note")

class HrEmploymentType(models.Model):
    _name = "hr.employment.type"

    name = fields.Char(string="Name")
    note = fields.Text(string="Note")


class HrFamily(models.Model):
    _name = "hr.family"

    employee_id = fields.Many2one("hr.employee", "Full name")
    name = fields.Char(string="Full name")
    dob = fields.Date(string="Date of birth")
    relationship_id= fields.Many2one('hr.family.relationship',string="Relationship")
    job= fields.Char(string="Job")
    workplace= fields.Char(string="Workplace")
    address= fields.Char(string="Address")
    note= fields.Char(string="Note")


class HrExperience(models.Model):
    _name = "hr.experience"

    employee_id = fields.Many2one("hr.employee", "Full name")
    experience_from_date = fields.Date(string="From date")
    experience_to_date = fields.Date(string="To date")
    work_experience= fields.Char(string="Work experience")
    place_of_work= fields.Char(string="Place of work")
    note= fields.Char(string="Note")

class HrEmployeeJob(models.Model):
    _name = "hr.employee.job"

    employee_id = fields.Many2one("hr.employee", "Full name")
    job_type = fields.Selection(related='job_id.type', string="From date")
    job_id = fields.Many2one('hr.job', string="Appointed position")
    allowance_coef = fields.Float(related='job_id.coefficient', string="Allowance coefficient")
    appointed_number = fields.Char(string="Appointed decision number")
    appointed_date = fields.Date(string="Appointed date")
    appointed_description = fields.Char(string="Appointed description")
    appointed_file = fields.Binary(string="Appointed file")
    dismissed_num = fields.Char(string="Dismissed decision number")
    dismissed_date = fields.Date(string="Dismissed date")
    dismissed_description = fields.Char(string="Dismissed description")
    dismissed_file = fields.Binary(string="Dismissed file")

