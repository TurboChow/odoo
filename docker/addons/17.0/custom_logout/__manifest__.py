{
    'name': 'Custom Logout',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Customize logout URL',
    'summary':'A module to customize the logout URL in Odoo',#简短说明
    'description': """A module to customize the logout URL in Odoo""",
    'author': '南京联成科技发展股份有限公司',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'views/custom_logout_template.xml',
    ],
    'installable': True,
    'application': False,
    'maintainer': '南京联成科技发展股份有限公司',  # 模块的维护者信息
    'author': '南京联成科技发展股份有限公司',  # 模块的作者信息
    'website': 'http://www.lsmsp.cn',  # 作者或模块相关网站
}