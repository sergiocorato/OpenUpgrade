# -*- coding: utf-8 -*-
# Copyright 2018 Eficent <http://www.eficent.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

_column_renames = {
    'maintenance_equipment': [
        ('warranty', 'warranty_date'),
    ],
    'maintenance_request': [
        ('technician_user_id', 'user_id'),
    ],
}

_model_renames = [
    ('machine.repair', 'maintenance.equipment'),
]

_table_renames = [
    ('machine_repair', 'maintenance_equipment'),
]


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr
    if openupgrade.table_exists(cr, 'machine_repair'):
        openupgrade.rename_models(cr, _model_renames)
        openupgrade.rename_tables(cr, _table_renames)
    openupgrade.rename_columns(cr, _column_renames)
