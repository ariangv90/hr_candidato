from odoo import api, models, fields

#Este es para saber si es un server, Firewall
class typeequipment(models.Model):
    _name = 'res.type.equipment'
    _description = ''

    name = fields.Char(string='Name')

    description = fields.Text(string='Description')

class OS(models.Model):
    _name = 'res.os'
    _description = ''

    name = fields.Char(string='Name OS')

    arch = fields.Selection([
        ('x86','x86'),
        ('x64', 'x64'),
    ],
        string='Arch OS')

    description = fields.Text(string='Description')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', '¡The code areadly exists!')
    ]

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
    nivel_parent = fields.Many2one('res.equipment',string='Top Equipment')

    networkcard = fields.Many2many('res.network.card',string='Network Card')

    gateway = fields.Char(string='Gateway',readonly=True)

    #Server o pc
    #Ram
    brand_ram = fields.Char(string='Brand Ram')
    speed_ram = fields.Float(string='Size Ram')
    fre_ram = fields.Float(string='Fre Ram')
    cont_ram = fields.Float(string='Cont Ram')
    socket_ram = fields.Float(string='Cont Socket Ram')

    #Disk
    brand_disk = fields.Char(string='Brand  Disk')

    size = fields.Float(string='Size Disk')

    array1 = fields.Selection([
        ('Raid','Raid'),
        ('GPT', 'GPT'),
        ('MBR', 'MBR'),
                               ]
    ,string='Array Disk')
    cont_disk = fields.Float(string='Cont Disk')
    #System OS
    os_ids = fields.Many2one('res.os',string='SO')

    #Switch o Router
    brand_router = fields.Char(string='Brand Router')
    red_line_id = fields.Many2one('res.line',string='Applicant Line')
    speed = fields.Float(string='Speed Line',readonly=True)
    type_connetion = fields.Float(string='Type Conection', readonly=True)


