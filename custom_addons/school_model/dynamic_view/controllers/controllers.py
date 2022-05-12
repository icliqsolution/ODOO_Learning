# -*- coding: utf-8 -*-
# from odoo import http


# class DynamicView(http.Controller):
#     @http.route('/dynamic_view/dynamic_view', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dynamic_view/dynamic_view/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dynamic_view.listing', {
#             'root': '/dynamic_view/dynamic_view',
#             'objects': http.request.env['dynamic_view.dynamic_view'].search([]),
#         })

#     @http.route('/dynamic_view/dynamic_view/objects/<model("dynamic_view.dynamic_view"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dynamic_view.object', {
#             'object': obj
#         })
