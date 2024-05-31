# custom_title_module/__manifest__.py
{
    'name': 'Custom Title Module',
    'version': '1.0',
    'depends': ['base', 'web', 'mail', 'account', 'sale', 'purchase', 'stock', 'hr', 'crm', 'website'],

    'data': [
        'views/custom_title_templates.xml',
    ],
    'installable': True,
    'application': True,
}
