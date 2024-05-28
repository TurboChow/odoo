{
    'name': 'Custom Auto Login',
    'version': '1.0',
    'category': 'Services',     #用于在应用列表中对模块进行分类
    'depends': ['web'],
    'data': [],
    'installable': True,        #模块是否可安装
    'auto_install': False,      #模块是否自动安装
    'license': 'LGPL-3',
    'application': True,        #是否显示在apps列表里面
    'summary':'A module for auto login using session_id',#简短说明
    'description':"""
        ========================
        This module allows users to automatically log in using a session_id
    """,                                    #详细说明
    'maintainer':'南京联成科技发展股份有限公司', #模块的维护者信息
    'author':'南京联成科技发展股份有限公司',     #模块的作者信息
    'website':'http://www.lsmsp.cn',               #作者或模块相关网站
}
