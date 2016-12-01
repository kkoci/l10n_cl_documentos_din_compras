# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class l10n_cl_documentos_din_compras(models.Model):
#     _name = 'l10n_cl_documentos_din_compras.l10n_cl_documentos_din_compras'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100