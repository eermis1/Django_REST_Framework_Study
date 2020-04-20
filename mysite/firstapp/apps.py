from django.apps import AppConfig


class FirstappConfig(AppConfig):
    name = 'firstapp'
    def ready(self):
        from django.contrib.auth.models import User
        from actstream import registry
        registry.register(self.get_model('Community'))
        registry.register(self.get_model('Post'))
        registry.register(self.get_model('Comment'))
        registry.register(User)
