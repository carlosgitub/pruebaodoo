# -*- coding: utf-8 -*-
{
    'name': "Gestion Prueba",

    'summary': """
       Gestion Facturacion
       """,

    'description': """
        Gestion Facturacion
    """,

    'author': "Carlos Diaz",
    'website': "https://www.mywebnow.now",
    'category': 'Gestion Lineas Factura',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base"],

    # always loaded
    'data': [
        "data/data.xml",
        "security/ir.model.access.csv",
        "views/lineas_factura_view.xml",
        "views/facturacion_view.xml",
    ],
}