# -*- coding: utf-8 -*-

from odoo import models, fields, api



class areac(models.Model):
    _name = 'areac.areac'
    _description = 'Areas of regulation and control'

    name = fields.Char(
        string='Name'
    )
    code = fields.Integer(
        string='Code'
    )
    ueb = fields.Many2one(
        'ueb.ueb',string='UEB'
    )
    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'The code already exists'),
        ('name_unique', 'UNIQUE (name)', 'The name already exists'),
    ]

class hrjob(models.Model):
    _inherit = 'hr.job'


    code = fields.Integer(
        string='Code'
    )

    area = fields.Many2one(
        'areac.areac', string='Areas of regulation and control'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'The code already exists'),
    ]