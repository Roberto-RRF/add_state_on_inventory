{
    'name': 'Agregar Estado Republica Invetario',
    'version': '1.0',
    'author':'ANFEPI: Roberto Requejo Fernández',
    'depends': ['stock'],
    'description': """
        Este módulo personaliza la vista de selección de acciones agregando el campo 'estado' a 
        la vista de árbol y habilitando la agrupación por el campo 'estado' en la vista de búsqueda.
    """,
    'data': [
        'views/stock_vpicktree_views.xml'
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    "license": "AGPL-3",
}