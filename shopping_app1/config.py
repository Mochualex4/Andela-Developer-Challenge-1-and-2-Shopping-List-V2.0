class Config(object):
    """
    Add the most common configurationns here that will common across all environments
    """

class ShoppingAppDevelopmentConfig(Config):
    """
    Shopping app development configurations to be added here
    """
    DEBUG = True

class ShoppingAppProductionConfig(Config):
    """
    Shopping app production configurations
    """
    DEBUG = False

app_config = {
    'development' : ShoppingAppDevelopmentConfig,
    'production' : ShoppingAppProductionConfig 
}
