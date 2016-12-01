# -*- coding: utf-8 -*-
from openerp import http

# class L10nClDocumentosDinCompras(http.Controller):
#     @http.route('/l10n_cl_documentos_din_compras/l10n_cl_documentos_din_compras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_documentos_din_compras/l10n_cl_documentos_din_compras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_documentos_din_compras.listing', {
#             'root': '/l10n_cl_documentos_din_compras/l10n_cl_documentos_din_compras',
#             'objects': http.request.env['l10n_cl_documentos_din_compras.l10n_cl_documentos_din_compras'].search([]),
#         })

#     @http.route('/l10n_cl_documentos_din_compras/l10n_cl_documentos_din_compras/objects/<model("l10n_cl_documentos_din_compras.l10n_cl_documentos_din_compras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_documentos_din_compras.object', {
#             'object': obj
#         })