# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class Line_factura(models.Model):
    _name = 'prueba.lineas_factura'
    _description = 'Gestion lineas_factura'

    name = fields.Char(string="Cantidad", help="Introduce la cantidad", size=20,
                       default="Cantidad")
    active = fields.Boolean(string="Active", default=True)
    codigo = fields.Char("Codigo")

    _sql_constraints = [
        ('lineas_factura_name_uniq',
         'unique (name)',
         'Nombre tiene que ser unico.')
    ]

    tag_ids = fields.Many2many(
        comodel_name="lineas_factura.tag"
    )

    @api.constrains('codigo')
    def _check_codigo(self):
        # comoprobamos que sea unica
        domain = [
            ('codigo', '=', self.codigo),
            ('id', '!=', self.id),
        ]
        lineas_facturas = self.search(domain)
        if lineas_facturas:
            raise exceptions.ValidationError("Codigo duplicado")


class Lineas_facturasTag(models.Model):
    _name = "lineas_factura.tag"

    name = fields.Char(string="Name")
