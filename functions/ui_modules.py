from tornado.web import UIModule


class NavModule(UIModule):
    def render(self, total_page, page, limit, nav_url):
        return self.render_string('common/modules/nav.html', total_page=total_page, page=page, limit=limit, nav_url=nav_url)
