from django.db import models
from abc import abstractmethod


class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=False,
        verbose_name="Is Active",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
    )

    class Meta:
        abstract = True
        ordering = ("pk",)

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("Implement __str__ method")
    
