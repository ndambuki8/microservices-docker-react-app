# services/users/projectc/config.py

class BaseConfig:
    """Base configuration"""
    TESTING = False

class DevelopmentConfig:
    """Development configuration"""
    pass

class TestingConfig:
    """Testing configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass

