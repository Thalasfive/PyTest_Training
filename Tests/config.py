class Config:
    def __init__(self, env='qa'):
        self.base_url = {
            'dev': 'https://myde-env.com',
            'qa': 'https://myqa-env.com',
        }[env]

        self.app_port = {
            'dev':8080,
            'qa':80
        }[env]