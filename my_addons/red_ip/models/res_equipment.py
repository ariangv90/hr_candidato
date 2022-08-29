from odoo import api, models, fields
import platform
import subprocess
import dns.resolver

#Este es para saber si es un server, Firewall
class typeequipment(models.Model):
    _name = 'res.type.equipment'
    _description = ''
    _rec_name = 'name'

    name = fields.Char(string='Name')

    description = fields.Text(string='Description')

class OS(models.Model):
    _name = 'res.os'
    _description = ''
    _rec_name = 'name'

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
    _rec_name = 'ip'

    ip = fields.Char(string='IP')

    brand = fields.Char(string='Brand')

    speed = fields.Float(string='Speed')

    gateway = fields.Char(string='Gateway')

    description = fields.Text(string='Description')

    _sql_constraints = [
        ('ip_uniq', 'unique(ip)', '¡The code areadly exists!')
    ]

class resequipment(models.Model):
    _name='res.equipment'
    _description = ''
    _rec_name = 'name_complete'

    code = fields.Char(string='Code')

    name = fields.Char(string='Name')

    name_dns = fields.Char(string='Name DNS')

    name_complete = fields.Char(string='Name Complete',store=True)

    type_equipment = fields.Selection([
        ('ROUTER','ROUTER'),
        ('SWITCH', 'SWITCH'),
        ('PC', 'PC'),
        ('SERVER', 'SERVER'),
    ],
        string='Type Equipment')
    #Este le da el gateway
    nivel_parent = fields.Many2one('res.equipment',string='Top Equipment')

    networkcard = fields.Many2many('res.network.card',string='Network Card')

    gateway = fields.Char(string='Gateway',store=True)

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
    os_ids = fields.Many2one('res.os',string='S.O')

    #Switch o Router
    brand_router = fields.Char(string='Brand Router')

    red_line_id = fields.Many2one('res.line',string='Applicant Line')

    speed = fields.Float(string='Speed Line',readonly=True)

    type_connetion = fields.Float(string='Type Conection', readonly=True)

    _sql_constraints = [
        ('networkcard_uniq', 'unique(networkcard)', '¡The code areadly exists!'),
        ('code_uniq', 'unique(code)', '¡The code areadly exists!'),
        ('name_uniq', 'unique(name)', '¡The code areadly exists!')
    ]

    @api.onchange('networkcard')
    def change_gateway(self):
        for p in self.networkcard:
            self.gateway = p.gateway

    @api.onchange('name', 'name_dns')
    def _compute_name(self):
        valor=""
        for name in self:
            valor = str(name.name) + "." + str(name.name_dns)
            name.name_complete = valor

    def server_ping(self):
        valor = False
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'

        command = ['ping', parameter, '1', '127.0.0.1']
        response = subprocess.call(command)

        if response == 0:
            valor=True
        else:
            valor = False

        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': ('Request success'),
                'message': 'PING: '+ str(valor),
                'sticky': False,
                'type': 'success'
            },
        }
        return notification

    def server_nsloockup(self):
        valor = ""
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = ['1.1.1.1', '8.8.8.8']
            result = resolver.query("www.google.com", 'A')
            for val in result:
                valor = val.to_text()
        except dns.resolver.NoAnswer:
            pass
            print(dns.resolver.NoAnswer)
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': ('Request success'),
                'message': 'nsLOOcKUP: '+ str(valor),
                'sticky': False,
                'type': 'success'
            },
        }
        return notification