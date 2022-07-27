# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rescompany(models.Model):
     _inherit='res.company'
     _description = 'Company'

     code = fields.Integer(
          string='Code'
     )

     _sql_constraints = [
          ('code_unique', 'UNIQUE (code)', 'Tag name already exists'),
     ]



