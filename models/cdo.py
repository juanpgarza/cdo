# -*- coding: utf-8 -*-

from odoo import models, fields, api

###### TRANSACCION

class CdoContrato(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.contrato'
    _rec_name = 'referencia'

    referencia = fields.Char('Referencia')
    order_id = fields.Many2one('sale.order', string='Orden Venta')
    cliente_id = fields.Many2one('res.partner', string='Cliente', domain="[('is_company','=',True)]")

    alta_ids = fields.One2many('cdo.alta', 'contrato_id')
    mensual_ids = fields.One2many('cdo.mensual', 'contrato_id')

    fecha_contrato =fields.Date('Fecha contrato')

class CdoRequisitoContrato(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.requisito.contrato'
    _rec_name = 'requisito_id'

    hr_alta_id = fields.Many2one('cdo.hr.alta',string='Recurso')
    hr_mensual_id = fields.Many2one('cdo.hr.mensual', string='Mensual')
    requisito_id = fields.Many2one('cdo.requisito', string='Requisito')

    alta_id = fields.Many2one('cdo.alta',related='hr_alta_id.alta_id', string='Alta', readonly=True)
    referencia_contrato_alta = fields.Char(related='hr_alta_id.alta_id.contrato_id.referencia', string='Contrato')
    interno_externo = fields.Selection(related='hr_alta_id.partner_id.tipo_recurso', string='Interno/Externo')

    requisito_cumplido = fields.Boolean('Requisito cumplido?')

    # adjunto_id = fields.Many2many('ir.attachment', 'cdo_requisito_contrato_adjunto_rel', 
    #                                     'requisito_contrato_id', 'attach_id3', string="Adjunto",
    #                                      help='Adjuntar archivos', copy=False)

    adjunto_id = fields.Many2one('ir.attachment', string="Adjunto")

    imagen1 = fields.Binary('Imagen1')

    @api.onchange('imagen1')   
    def imagen1_change(self):        
        if self.imagen1:
            self.requisito_cumplido = True
        else:
            self.requisito_cumplido = False
                
        return
    
    @api.multi
    def write(self, vals):
        super(CdoRequisitoContrato, self).write(vals)
        
        requisitos_cumplidos = True
        for requisito in self.hr_alta_id.requisito_contrato_ids:
            if not requisito.requisito_cumplido:
                requisitos_cumplidos = False
                break
        
        if requisitos_cumplidos:
            self.hr_alta_id.requisitos_cumplidos = True

            requisitos_hr_cumplidos = True
            for hr_alta in self.hr_alta_id.alta_id.hr_alta_ids:
                if not hr_alta.requisitos_cumplidos:
                    requisitos_hr_cumplidos = False
                    break
            
            if requisitos_hr_cumplidos:
                self.hr_alta_id.alta_id.requisitos_cumplidos = True
        else:
            self.hr_alta_id.requisitos_cumplidos = False
            self.hr_alta_id.alta_id.requisitos_cumplidos = False

        return True

class Adjunto(models.Model):
    _inherit = 'ir.attachment'

    requisito_ids = fields.One2many('cdo.requisito.contrato','adjunto_id')

    # doc_attach_rel = fields.Many2many('cdo.requisito.contrato', 'adjunto_id', 'attach_id3', 'requisito_contrato_id',
    #                                   string="Adjuntar archivos", invisible=1)
""" 
    @api.model
    def create(self, vals):

        nuevo = super(Adjunto, self).create(vals)

        # id = nuevo.doc_attach_rel.requisito_contrato_id.id

        import pdb; pdb.set_trace() """


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
    observaciones = fields.Char('Observaciones')

class CdoHrTipoTarea(models.Model):
    _inherit = ['mail.thread']
    _name = 'cdo.hr.tipo.tarea'
    _rec_name = 'descripcion'

    descripcion = fields.Char('Descripción')
