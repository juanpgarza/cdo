# -*- coding: utf-8 -*-

from odoo import models, fields, api

def get_years():
    year_list = []
    for i in range(2018, 2036):
        year_list.append((i, str(i)))
    return year_list

class CdoMensual(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.mensual'
    _rec_name = 'id'

    contrato_id = fields.Many2one('cdo.contrato', string='Contrato')

    hr_mensual_ids = fields.One2many('cdo.hr.mensual', 'mensual_id')

    mes = fields.Selection([(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
                            (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), 
                            (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'), ], 
                            string='Mes', default=lambda self: self._get_default_mes_actual())

    anio = fields.Selection(get_years(), string='Año',default=lambda self: self._get_default_anio_actual())

class CdoHrMensual(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.hr.mensual'

    mensual_id = fields.Many2one('cdo.mensual',string='Mensual')

    requisito_contrato_ids = fields.One2many('cdo.requisito.contrato', 'hr_mensual_id')

    