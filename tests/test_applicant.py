from odoo.tests.common import TransactionCase
from odoo.tests import tagged

@tagged('-at_install', 'post_install')
class ApplicantTestCase(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(ApplicantTestCase, self).setUp(*args, **kwargs)
        self.test_applicant = self.env['hr.applicant'].create({'name': 'Name 1'})
