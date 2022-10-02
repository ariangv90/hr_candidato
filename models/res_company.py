# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rescompany(models.Model):
     _inherit = "res.company"


     code = fields.Integer(
          string = "Code"
     )

     _sql_constraints = [
          ('code_unique', 'UNIQUE (code)', 'The code already exists'),
     ]



