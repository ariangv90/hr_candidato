# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrApplicants(models.Model):
     _inherit = 'hr.applicant'
     _description = 'Gestion of Applicants'

     ci = fields.Char(
          string='CI'
     )

     address = fields.Char(
          string='Home address'
     )

     grade_possesses = fields.Char(
          string='Formal Grade That You Possess'
     )

     experience = fields.Text(
          string='Experience that you possess'
     )

     formal_grade = fields.Char(
          string='Formal grade'
     )

     Observations = fields.Text(
          string='Observations'
     )

     course = fields.Many2one(
          'slide.channel',
          string='Course of Habilitation',
     )

     _sql_constraints = [
          ('ci_unique', 'UNIQUE (ci)', 'Tag name already exists'),
     ]