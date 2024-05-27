from odoo import http
from odoo.http import request
import requests
import logging

_logger = logging.getLogger(__name__)


class CustomAutoLoginController(http.Controller):

    @http.route('/custom_auto_login', type='http', auth="none", csrf=False)
    def custom_auto_login(self, login=None, password=None, db=None, redirect='/web'):
        _logger.info("Custom auto login called")
        _logger.info("Login: %s", login)
        _logger.info("Database: %s", db)
        if not login or not password or not db:
            _logger.error("Missing parameters: login, password, or db")
            return "Missing parameters: login, password, or db"

        try:
            base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
            url = f"{base_url}/web/session/authenticate"
            _logger.info("Authentication URL: %s", url)
            headers = {'Content-Type': 'application/json'}
            payload = {
                'jsonrpc': '2.0',
                'method': 'call',
                'params': {
                    'db': db,
                    'login': login,
                    'password': password
                },
                'id': None,
            }
            _logger.info("Payload: %s", payload)
            response = requests.post(url, json=payload, headers=headers)
            _logger.info("Response: %s", response.text)
            result = response.json()

            if 'result' in result:
                user_id = result['result']['uid']
                _logger.info("Authenticated user_id: %s", user_id)

                # 手动设置会话
                request.session.authenticate(db, login, password)
                _logger.info("Session ID: %s", request.session.sid)

                # 使用 http.redirect 进行重定向
                return request.redirect(redirect)
            else:
                error = result.get('error')
                _logger.error("Failed to authenticate: %s", error)
                return f"Failed to authenticate: {error}"
        except Exception as e:
            _logger.exception("Error during authentication")
            return f"Internal server error: {str(e)}"