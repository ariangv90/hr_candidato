from odoo import api, models, fields

#Este es para saber si es un server, Firewall
class typeequipment(models.Model):
    _name = 'res.type.equipment'
    _description = ''

    name = fields.Char(string='Name')

    description = fields.Text(string='Description')


class networkcard(models.Model):
    _name = 'res.network.card'
    _description = ''

    ip = fields.Char(string='IP')

    brand = fields.Char(string='Brand')

    speed = fields.Float(string='Speed')

    description = fields.Text(string='Description')

    _sql_constraints = [
        ('ip_uniq', 'unique(ip)', '¡The code areadly exists!')
    ]

class equipment(models.Model):
    _name='res.equipment'
    _description=''

    type_equipment = fields.Many2one('res.type.equipment')
    #Este le da el gateway
    nivel = fields.Many2one('res.equipment',string='Top Equipment')

    networkcard = fields.Many2many('res.network.card',string='Network Card')

    gateway = fields.Char(string='Gateway',readonly=True)

    #Server o pc

    #Switch

    #Router
