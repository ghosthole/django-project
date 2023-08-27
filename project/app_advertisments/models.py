from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model  # получаем модель user'а
from django.utils import timezone

User = get_user_model()


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("title", max_length=128)
    description = models.TextField("description")       # 2 числа после запятой
    price = models.DecimalField("price", max_digits=10, decimal_places=2)  # float
    auction = models.BooleanField("auction", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)  # добавляет дату при создании поста
    updated_at = models.DateTimeField(auto_now=True)  # изменяет дату при изменении в посте
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # если user будет удален, то все связанные объявления
    # тоже удаляться
    image = models.ImageField("изображение", upload_to="advertisments/")

    @admin.display(description="Дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html("<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Дата изменения")
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            update_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html("<span style='color: yellow; font-weight: bold;'>Сегодня в {} </span>", update_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    # lesson 9 ex 4.1
    @admin.display(description="photo")
    def preview_image(self):
        if self.image:
            return format_html(f"<img src='{self.image.url}' width='120px' height='120px'>")
        return format_html("<img src='http://127.0.0.1:8000/media/advertisments/no_image.jpg' width='120px' height='120px'>")

    # lesson 7, ex 4
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"

