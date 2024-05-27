from odoo import http
from odoo.http import request


class CustomLogout(http.Controller):
    @http.route('/web/session/logout', type='http', auth="user")
    def web_logout(self, redirect=None):
        # 使当前用户会话过期
        request.session.logout()

        # 获取当前浏览器访问的主机名和端口
        host = request.httprequest.host

        # 自定义跳转路径
        #redirect_url = 'http://www.lsmsp.cn'
        redirect_url = f'http://{host}/www.lsmsp.cn'

        # Construct HTTP response with redirect status
        response = http.Response()
        # 302 Found (temporary redirect)
        response.status = 302
        response.headers['Location'] = redirect_url

        return response
