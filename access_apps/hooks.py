# Copyright 2021 Ivan Yelizariev <https://github.com/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
from odoo import SUPERUSER_ID, api


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    access = env.ref(
        "base.access_ir_module_module_group_user", raise_if_not_found=False
    )
    access.write({"active": True})
