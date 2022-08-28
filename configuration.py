class ConfiguracionBase(object):
    'Configuración Base'
    SECRET_KEY = 'aakeqll-Q2*--++FFhY'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://usuario:clave-@localhost:3306/Recetario?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class ConfiguracionProduccion(ConfiguracionBase):
    'Configuración Producción'
    DEBUG = False

class ConfiguracionDesarrollo(ConfiguracionBase):
    'Configuración de Desarrollo'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Clave_desarrollo'
