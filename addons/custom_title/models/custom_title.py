# my_module/models/my_model.py
from odoo import models

class MyCustomModule(models.AbstractModel):
    _name = 'custom.title'
    _description = 'Custom Title'

    @staticmethod
    def _get_my_title():
        return 'My New Title'
