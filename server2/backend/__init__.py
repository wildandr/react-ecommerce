from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('.models')

        # Konfigurasi SQLAlchemy
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine

        #add routes



        config.add_route('products', '/products')
        config.add_route('product', '/products/{id}')

        config.add_route('orders', '/orders')
        config.add_route('order', '/orders/{id}')

        config.add_route('users', '/users')
        config.add_route('user', '/users/{id}')

        config.add_route('deliveries', '/deliveries')
        config.add_route('delivery', '/deliveries/{id}')

        config.add_route('payments', '/payments')
        config.add_route('payment', '/payments/{id}')
    

        config.scan()
    return config.make_wsgi_app()
