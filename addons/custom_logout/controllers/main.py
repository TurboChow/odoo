from odoo import http
from odoo.http import request
from urllib.parse import urlsplit, urlunsplit

class CustomLogout(http.Controller):
    @http.route('/web/session/logout', type='http', auth="user")
    def web_logout(self, redirect=None):
        # 使当前用户会话过期
        request.session.logout()

        # 获取当前浏览器访问的主机名和端口
        host = request.httprequest.host

        # 自定义跳转路径
        #redirect_url = 'http://www.lsmsp.cn'

        # 自定义跳转路径，带端口号
        #redirect_url = f'http://{host}/avatar-digital-management-web/#/login'

        #自定义跳转路径，不带端口号
        host_without_port = urlsplit(f'http://{host}').hostname
        redirect_url = f'http://{host_without_port}/avatar-digital-management-web/#/login?from2ccp=hsnotk'



        # Construct HTTP response with redirect status
        response = http.Response()
        # 302 Found (temporary redirect)
        response.status = 302
        response.headers['Location'] = redirect_url

        return response
