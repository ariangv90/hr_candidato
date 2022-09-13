from odoo import models, fields, api
from odoo.exceptions import Warning


class ueb(models.Model):
    _name = 'ueb.ueb'
    _description = 'UEB'

    name = fields.Char(
        string='Name'
    )
    code = fields.Integer(
        string='Code'
    )
    company = fields.Many2one(
        'res.company',
        string='Company Inside'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'Tag code already exists'),
        ('name_unique', 'UNIQUE (name)', 'Tag name already exists'),
    ]
    @api.model
    def create(self,vals):
        print('User',self.env.user.name)
        print('User', self.env.context)

        vals['code']=vals['code']+1
        print(vals['code'],type(vals['code']))
        return super(ueb,self).create(vals)


    def action_server(self):
        cont = 0
        for i in self:
            print(i.name,i.code,i.company)
            cont = cont+1

        notification = {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': ('Request success'),
                    'message': 'UEB: '+self.name+" "+self.code,
                    'sticky': False,
                    'type': 'success'
        },
        }
        return notification
        #raise Warning('Funcionan los records server'+self.name+'')

class stage(models.Model):
    _inherit= 'hr.recruitment.stage'
    _description = 'Stage of the process of selection'

    code = fields.Integer(
        string='Code'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'Tag name already exists'),
    ]
