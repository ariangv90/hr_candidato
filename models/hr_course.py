from odoo import models, fields, api



class aspectos(models.Model):
    _name = 'slide.aspect'
    _description = 'Aspect to evaluate course of habilitation'

    name = fields.Char(
        string='Name'
    )
    code = fields.Integer(
        string='Code'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'Tag name already exists'),
        ('name_unique', 'UNIQUE (name)', 'Tag name already exists'),
    ]

class course(models.Model):
    _inherit = 'slide.channel'
    _description = 'Course of habilitation'


    code = fields.Integer(
        string='Code'
    )
    aspectos = fields.Many2one(
        'slide.aspect',
        string='Aspect to evaluate course of habilitation'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'Tag name already exists'),
        ('name_unique', 'UNIQUE (name)', 'Tag name already exists'),
    ]