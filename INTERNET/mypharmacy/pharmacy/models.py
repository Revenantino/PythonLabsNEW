from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Medicine(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Назва")
    slug = models.SlugField(max_length=200, db_index=True)
    content = models.TextField(blank=True, verbose_name="Вміст")
    manufacturer_name = models.CharField(max_length=200, verbose_name="Виробник")
    indications_for_use = models.TextField(blank=True, verbose_name="Показання для застосування")
    contraindications = models.TextField(blank=True, verbose_name="Протипоказання")
    application_and_dose = models.TextField(blank=True, verbose_name="Спосіб застосування та дози")
    term = models.CharField(max_length=200, verbose_name="Термін дії")
    storage = models.TextField(blank=True, verbose_name="Умови зберігання")
    available_quantity = models.PositiveIntegerField(verbose_name="Кількість на складі")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    img = models.ImageField(upload_to='medicines/%Y/%m/%d/', blank=True, verbose_name="Зображення")
    available = models.BooleanField(default=True, verbose_name="Доступний")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id']
        ]

    def get_absolute_url(self):
        return reverse('pharmacy:MedicineDetail', args=[self.id, self.s])

    def __str__(self):
        return self.name
