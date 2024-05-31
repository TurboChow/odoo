from odoo import http
from odoo.http import request
import logging
from urllib.parse import urlsplit
_logger = logging.getLogger(__name__)


class CustomLoginRedirect(http.Controller):

    # session失效的时候强制跳转到ccp，避免跳转到odoo登录界面
    @http.route('/web/login', type='http', auth='public', website=True)
    def web_login(self, redirect=None, **kw):
        # custom_login_url = 'http://10.20.4.73/avatar-digital-management-web/#/login'
        host = request.httprequest.host
        custom_login_url = urlsplit(f'http://{host}').hostname
        custom_login_url = f'http://{custom_login_url}/avatar-digital-management-web/#/login?from2ccp=hsnotk'
        _logger.info(f"Redirecting to custom login URL: {custom_login_url}")
        # Return a page with JavaScript redirection
        return """
        <html>
            <head>
                <script type="text/javascript">
                    window.location.href = "%s";
                </script>
            </head>
            <body>
                If you are not redirected automatically, follow this <a href="%s">link</a>.
            </body>
        </html>
        """ % (custom_login_url, custom_login_url)
