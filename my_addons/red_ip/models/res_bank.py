from odoo import models, fields, api



class resBank(models.Model):
    _inherit = "res.bank"

    res_municipality_id = fields.Many2one('res.municipality', 'Municipality', domain="[('state_id', '=', state)]", help="Municipios de Cuba")

    code = fields.Integer(string='CODE')

    @api.onchange('state')
    def _onchange_state(self):
        if self.state.country_id:
            self.country = self.state.country_id
        self.res_municipality_id = ""

    _sql_constraints = [
        ('code_uniq', 'unique(code)', '¡The code areadly exists!')
    ]

