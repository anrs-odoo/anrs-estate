{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Manage our real estate',
    'description': "",
    'depends': [
        'base_setup',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml'
        'views/estate_menus.xml'
    ]
}
