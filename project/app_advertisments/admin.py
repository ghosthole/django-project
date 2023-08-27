from django.contrib import admin
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

    @admin.action(description="Убрать возможность торга")  # описание кнопки
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


# регистрация новой строчки, которая содержит данные класса Advertisement
admin.site.register(Advertisement, AdvertisementAdmin)
