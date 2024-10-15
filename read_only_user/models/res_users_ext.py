##############################################################################
#
# Copyright (c) 2017 brain-tec AG (http://www.braintec-group.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################

from odoo import fields, models


class ResUsersExt(models.Model):
    _inherit = "res.users"

    is_regular_user = fields.Boolean(string="Is Regular User", default=True)

    def toggle_regular_user(self):
        self.is_regular_user = not self.is_regular_user
