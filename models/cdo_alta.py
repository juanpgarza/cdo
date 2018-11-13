# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CdoAlta(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.alta'
    _rec_name = 'fecha_alta'
    
    contrato_id = fields.Many2one('cdo.contrato', string='Contrato')

    hr_alta_ids = fields.Many2one('cdo.hr.alta', 'alta_id')

    fecha_alta = fields.Date('Fecha alta')

    requisitos_completos = fields.Boolean('Requisitos Completos')

class CdoHrAlta(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.hr.alta'
    _rec_name = 'partner_id'

    alta_id = fields.Many2one('cdo.alta', string='Alta')
    tipo_recurso_id = fields.Many2one('cdo.tipo.recurso', string='Tipo de recurso')
    tipo_tarea_id = fields.Many2one('cdo.hr.tipo.tarea', string='Tipo de tarea')
    partner_id = fields.Many2one('res.partner', string='Recurso')

    requisito_contrato_ids = fields.One2many('cdo.requisito.contrato', 'hr_alta_id')

