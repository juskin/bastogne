from tornado.web import authenticated
from .base import BaseHandler


class AdminHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render('admin/index.html')

