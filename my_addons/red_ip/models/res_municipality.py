# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.osv import expression

class Municipality(models.Model):
    _name = 'res.municipality'
    _description = 'Municipio'
    _order = 'code'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', help='The code of municipality', required=True)
    country_id = fields.Many2one('res.country', string='Country', required=True)
    state_id = fields.Many2one('res.country.state', 'State', domain="[('country_id', '=', country_id)]")
#    zipcode = fields.Many2one('res.city', string='Zip')

    _sql_constraints = [
        ('name_code_uniq', 'unique(state_id, code)', '¡The code areadly exists!')
    ]

class Partner(models.Model):
        _inherit='res.partner'

        res_municipality_id = fields.Many2one('res.municipality',string='Municipality')