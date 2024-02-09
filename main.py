# import flet as ft
# from router_tev import Router
#
#
# def main(page: ft.Page):
#     page.title = "Routes Example"
#     # page.theme_mode = "dark"
#
#     myrouter = Router(page)
#     page.on_route_change = myrouter.route_change
#     page.on_view_pop = myrouter.view_pop
#     page.go(page.route)
#
#
# if __name__ == '__main__':
#     # ft.app(target=main, assets_dir="assets")
#     ft.app(target=main, view=ft.AppView.WEB_BROWSER)

import flet as ft
from views.routes import router
from app_bar import NavBar


def main(page: ft.Page):


    page.theme_mode = "dark"
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/')

ft.app(target=main, assets_dir="assets")