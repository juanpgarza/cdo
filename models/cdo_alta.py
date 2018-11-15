# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CdoAlta(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.alta'
    _rec_name = 'fecha_alta'
    
    contrato_id = fields.Many2one('cdo.contrato', string='Contrato')

    hr_alta_ids = fields.One2many('cdo.hr.alta', 'alta_id')

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

    referencia_contrato = fields.Char(related='alta_id.contrato_id.referencia', string='Contrato')
    interno_externo = fields.Selection(related='partner_id.tipo_recurso', string='Interno/Externo')

    requisitos_cumplidos = fields.Boolean('Requisitos cumplidos?')

    @api.model
    def create(self, vals):

        nuevo = super(CdoHrAlta, self).create(vals)

        # esta parte es un poco más complicada. Por ahora no estoy teniendo en cuenta el tipo de recurso, ni la tarea.
        requisitos_ids = self.env['cdo.requisito'].search([('requisito_alta','=',True)])

        for requisito in requisitos_ids:
            vals1 = {'hr_alta_id': nuevo.id,'requisito_id': requisito.id}
            self.env['cdo.requisito.contrato'].create(vals1)

        return nuevo