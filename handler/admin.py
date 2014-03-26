from .base import BaseHandler


class AdminHandler(BaseHandler):
    def get(self):
        self.render('admin/index.html')

