{
    'name': 'Custom Logout',
    'version': '1.0',
    'category': 'Services',                                 #用于在应用列表中对模块进行分类
    'summary': 'Customize logout URL',
    'summary':'A module to customize the logout URL in Odoo',#简短说明
    'description': """A module to customize the logout URL in Odoo""",
    'author': '南京联成科技发展股份有限公司',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'views/custom_logout_template.xml',
    ],
    'installable': True,                        #模块是否可安装
    'auto_install': False,                     #模块是否自动安装
    'application': True,                       #是否显示在apps列表里面
    'maintainer': '南京联成科技发展股份有限公司',  # 模块的维护者信息
    'author': '南京联成科技发展股份有限公司',  # 模块的作者信息
    'website': 'http://www.lsmsp.cn',  # 作者或模块相关网站
}