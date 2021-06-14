from .views import index

def setup_router(app):
    app.router.add_route('GET', r'/scan/{ip}/{begin_port}/{end_port}', index)
