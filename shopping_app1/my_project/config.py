class Config(object):
    """
    Common configurations
    """

class ShoppingAppDevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True

class ShoppingAppProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

shopping_app_config = {
    'development' : ShoppingAppDevelopmentConfig,
    'production' : ShoppingAppProductionConfig 
}
