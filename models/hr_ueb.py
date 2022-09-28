from odoo import models, fields, api
from odoo.exceptions import Warning



class ueb(models.Model):
    _name = "ueb.ueb"
    _description = "UEB"

    name = fields.Char(
        string = "Name"
    )
    code = fields.Integer(
        string = "Code"
    )
    company = fields.Many2one(
        "res.company",
        string = "Company Inside"
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE (code)', 'The code already exists'),
        ('name_unique', 'UNIQUE (name)', 'The name already exists'),
    ]
    @api.model
    def create(self,vals):
        print('User',self.env.user.name)
        print('User', self.env.context)

        vals['code']=vals['code']+1
        print(vals['code'],type(vals['code']))
        return super(ueb,self).create(vals)


    def action_server(self):
        cont = len(self)

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

