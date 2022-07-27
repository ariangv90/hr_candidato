from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged
from datetime import date
from odoo import fields

class ApplicantTestCase(TransactionCase):


    def setUp(self, *args, **kwargs):
        print('test')
        super(ApplicantTestCase, self).setUp(*args, **kwargs)
        # Add test setup code here...
        self.env['hr.applicant'].search([('ci', '=', "")]).write({'ci': "90070641462"})
        #Permisos
        user = self.env.ref('base.demo')
        t0 = date.today()
        Todo = self.env['hr.applicant'].sudo(user)
        self.todo1 = Todo.create({
            'name': 'Todo1',
            'date_deadline': fields.Date.to_string(t0)})

        self.todo2 = Todo.create({
            'name': 'Todo2'})

        applicant = self.env['hr.applicant'].sudo(user)
        self.applicant = applicant.create({})

