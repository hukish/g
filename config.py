class Config:
    SECRET_KEY = ('1234')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/events'
    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True