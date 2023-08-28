import datetime

from django.contrib import admin
from django.forms import DateField, DateTimeField
from django.utils import timezone

from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "description", "price", "created_date", "updated_date", "auction",
                    "preview_image"]
    list_filter = ["auction", "created_at", "updated_at"]
    actions = ["make_auction_as_false", "make_auction_as_true"]
    # кортеж, который позволяет обобщать строки при добавлении товара
    fieldsets = (
        ("Общее", {
            "fields": (
                "title", "description", "user", "image"
                       )
        }),
        ("Финансы", {  # Финансы здесь - название блока
            "fields": (
                "price", "auction"
            ),  # значение - какие строки хранить под этим блоком
            "classes": ["collapse"]  # отвечает за css-стили, которые можем применить
        })
    )

    @staticmethod
    def update_with_last_modified_time(qs, **kwargs):
        # This function adds any auto_now field to the update call because QuerySet.update() doesn't do it :X
        model_fields = qs.model._meta.get_fields()
        fields_and_value_map = {}
        for field in model_fields:
            try:
                auto_now = field.__getattribute__('auto_now')
            except AttributeError:
                auto_now = False

            if auto_now:
                if type(field) == DateField:
                    fields_and_value_map[field.name] = datetime.date.today()
                elif type(field) == DateTimeField:
                    fields_and_value_map[field.name] = timezone.now()

        fields_and_value_map.update(kwargs)
        return qs.update(**fields_and_value_map)

    @admin.action(description="Убрать возможность торга")  # описание кнопки
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
        self.update_with_last_modified_time(queryset)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
        self.update_with_last_modified_time(queryset)


# регистрация новой строчки, которая содержит данные класса Advertisement
admin.site.register(Advertisement, AdvertisementAdmin)
