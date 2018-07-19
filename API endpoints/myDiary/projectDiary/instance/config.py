import os
"""call for os environments."""


class Config(object):
    """Parent configuration."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Development Configurations."""

    DEBUG = True


class TestingConfig(Config):

    """Testing Configurations."""
    TESTING = True
    DEBUG = True


class StagingConfig(Config):

    """Staging Configurations."""
    DEBUG = True


class ProductionConfig(Config):
    """Production Configurations."""
    DEBUG = False
    TESTING = False


"""dictionary that stores environments."""
app_Config = {
    'staging': StagingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
