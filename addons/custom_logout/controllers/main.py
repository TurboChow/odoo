from odoo import http

class CustomLogout(http.Controller):
    @http.route('/web/session/logout', type='http', auth="user")
    def web_logout(self, redirect=None):

        # Perform any custom actions here
        # Custom redirect URL
        redirect_url = 'http://www.lsmsp.cn'  # 自定义跳转路径

        # Construct HTTP response with redirect status
        response = http.Response()
        response.status = 302  # 302 Found (temporary redirect)
        response.headers['Location'] = redirect_url

        return response
