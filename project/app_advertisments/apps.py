from django.apps import AppConfig


class AppAdvertismentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_advertisments"
    # change chapter name(lesson 8, ex 4)
    verbose_name = "Объявления"
