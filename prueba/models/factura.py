# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class Facturacion(models.Model):
    _name = 'prueba.factura'
    _description = 'Gestion Factura'

    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('confirmado', 'Confirmado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', readonly=True, index=True, copy=False,
        default='nuevo', tracking=True)

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(
        string="Name",
        help="Introduce el nombre",
        default="Nueva Orden Facturacion")
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Cliente")

    facturacion_line_ids = fields.One2many(
        comodel_name="prueba.factura.line",
        inverse_name="facturacion_id",
        string="lineas Reparacion"
    )

    notas = fields.Html(string="Notas")

    READONLY_STATES = {
        'nuevo': [('readonly', False)],
        'confirmado': [('readonly', True)],
        'cancelado': [('readonly', False)],
    }

    company_id = fields.Many2one('res.company', 'Empresa', required=True,
                                 index=True, states=READONLY_STATES,
                                 default=lambda self: self.env.company.id)


    @api.model
    def create(self, vals):
        new_seq_name = self.env['ir.sequence'].next_by_code(
            'factura') or 'New'
        vals.update(name=new_seq_name)
        res = super(Facturacion, self).create(vals)
        return res

    def confirm(self):
        self.write({'state': "confirmado"})


class FacturacionLine(models.Model):
    _name = 'prueba.factura.line'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(
        string="Producto",
        help="Introduce el nombre",
        default="Nuevo Producto")
    facturacion_id = fields.Many2one(comodel_name="prueba.factura")
    lineas_factura_id = fields.Many2one(
        comodel_name="prueba.lineas_factura", string="Lineas_factura")
