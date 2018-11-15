# -*- coding: utf-8 -*-

from odoo import models, fields, api

###### TRANSACCION

class ResPartner(models.Model):
    _inherit = ['res.partner']

    tipo_recurso = fields.Selection([(1, 'Recurso Interno'), (2, 'Recurso Externo')], 
                        string='Recurso')