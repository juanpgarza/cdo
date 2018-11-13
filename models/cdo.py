# -*- coding: utf-8 -*-

from odoo import models, fields, api

###### TRANSACCION

class CdoContrato(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.contrato'
    _rec_name = 'order_id'

    order_id = fields.Many2one('sale.order', string='Orden Venta')
    cliente_id = fields.Many2one('res.partner', string='Cliente', domain="[('is_company','=',True)]")

    alta_ids = fields.One2many('cdo.alta', 'contrato_id')
    mensual_ids = fields.One2many('cdo.mensual', 'contrato_id')

    fecha_contrato =fields.Date('Fecha contrato')

class CdoRequisitoContrato(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.requisito.contrato'

    hr_alta_id = fields.Many2one('cdo.hr.alta',string='Alta')
    hr_mensual_id = fields.Many2one('cdo.hr.mensual', string='Mensual')
    requisito_id = fields.Many2one('cdo.requisito', string='Requisito')

    requisito_cumplido = fields.Boolean('Requisito cumplido?')


###### CONFIGURACION

class CdoTipoRecursoRequisito(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.tipo.recurso.requisito'

    tipo_recurso_id = fields.Many2one('cdo.tipo.recurso', string='Tipo de Recurso')
    requisito_id = fields.Many2one('cdo.requisito', string='Requisito')

class CdoHrTipoTareaRequisito(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.hr.tipo.tarea.requisito'

    tipo_tarea_id = fields.Many2one('cdo.hr.tipo.tarea', string='Tipo de Recurso')
    requisito_id = fields.Many2one('cdo.requisito', string='Requisito')

class CdoRequisito(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.requisito'
    _rec_name = 'descripcion'

    descripcion = fields.Char('Descripción')
    requisito_alta = fields.Boolean('Requisito de alta?')
    requisito_mensual = fields.Boolean('Requisito mensual?')
    tiene_vencimiento = fields.Boolean('Tiene vencimiento?')

class CdoTipoRecurso(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.tipo.recurso'
    _rec_name = 'descripcion'

    descripcion = fields.Char('Descripción')

class CdoHrTipoTarea(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.hr.tipo.tarea'
    _rec_name = 'descripcion'

    descripcion = fields.Char('Descripción')
