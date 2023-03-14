from django.db import models
from django.core.validators import MinValueValidator


class TruckModel(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name="Название модели самосвала")
    capacity_tons = models.IntegerField(null=False,
                                        verbose_name="Максимальная загрузка самосвала данной модели в тоннах",
                                        validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель самосвалов'
        verbose_name_plural = 'Модели самосвалов'
        ordering = ["name"]


class Truck(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="Бортовой номер самосвала")
    truck_model = models.ForeignKey(TruckModel, on_delete=models.CASCADE, verbose_name="Модель самосвала")
    current_load_tons = models.IntegerField(verbose_name="Текущая загрузка самосвала в тоннах",
                                            validators=[MinValueValidator(0)])

    @property
    def overload_percents(self):
        """ Возвращает значение перегруза в процентах (на сколько процентов превышена).
            Если превышения по грузу нет, возвращаем 0. """

        current_utilization = self.current_load_tons / self.truck_model.capacity_tons * 100
        return round(current_utilization - 100, 2) if current_utilization > 100 else round(0, 0)

    @property
    def max_load_tons(self):
        return self.truck_model.capacity_tons

    def __str__(self):
        return "Самосвал с бортовым номером" + self.id

    class Meta:
        verbose_name = 'Самосвал'
        verbose_name_plural = 'Самосвалы'
        ordering = ["id"]
