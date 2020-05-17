from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    meta_description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products') # 카테고리를 삭제해도 보통 상품은 남아 있어야 하므로 SET_NULL
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id','slug']] # 멀티 컬럼 색인. id와 slug를 묶어서 색인이 가능하도록

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
