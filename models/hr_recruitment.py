# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrApplicants(models.Model):
     _inherit = "hr.applicant"

     ci = fields.Char(
          string = "CI"
     )

     address = fields.Char(
          string = "Home address"
     )

     grade_possesses = fields.Char(
          string = "Formal Grade That You Possess"
     )

     experience = fields.Text(
          string = "Experience that you possess"
     )

     formal_grade = fields.Char(
          string = "Formal grade"
     )

     Observations = fields.Text(
          string = "Observations"
     )

     course = fields.Many2one(
          "slide.channel",
          string = "Course of Habilitation",
     )

     _sql_constraints = [
          ('ci_unique', 'UNIQUE (ci)', 'The ci already exists'),
     ]


class stage(models.Model):
    _inherit = "hr.recruitment.stage"

    code = fields.Integer(
        string = "Code"
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'Tag code already exists'),
    ]


class hrjob(models.Model):
    _inherit = "hr.job"


    code = fields.Integer(
        string = "Code"
    )

    area = fields.Many2one(
        "areac.areac",
        string = "Areas of regulation and control"
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'The code already exists'),
    ]