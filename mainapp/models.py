from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:

    objects = LatestProductsManager()


class CategoryManager(models.Manager):

    CATEGORY_NAME_COUNT_NAME = {
        'Ноутбуки': 'notebook__count',
        'Смартфоны': 'smartphone__count',
        'Десктопы': 'desktop__count',
        'Планшеты': 'tablet__count',
        'Телевизоры': 'television__count',
        'Аудиотехника': 'audio__count',
        'Фототехника': 'photographic__count',
        'Офисная техника': 'office__count',
        'Бытовая техника': 'appliances__count',
        'Программное обеспечение': 'software__count'
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_models_for_count('notebook', 'smartphone', 'desktop', 'tablet', 'television', 'audio', 'photographic', 'office', 'appliances', 'software')
        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
        ]
        return data


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self.__class__.__name__.lower()


class Notebook(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процессора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    video = models.CharField(max_length=255, verbose_name='Видеокарта')
    time_without_charge = models.CharField(max_length=255, verbose_name='Время работы аккумулятора')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Desktop(Product):

    model_proc = models.CharField(max_length=255, verbose_name='Модель Процессора')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процессора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    video = models.CharField(max_length=255, verbose_name='Видеокарта')
    block_pitania = models.CharField(max_length=255, verbose_name='Блок питания')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Smartphone(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    resolution = models.CharField(max_length=255, verbose_name='Разрешение экрана')
    accum_volume = models.CharField(max_length=255, verbose_name='Объем батареи')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    sd = models.BooleanField(default=True, verbose_name='Наличие SD карты')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процессора')
    sd_volume_max = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Максимальный объем встраивамой памяти'
    )
    main_cam_mp = models.CharField(max_length=255, verbose_name='Главная камера')
    frontal_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальная камера')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Tablet(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    resolution = models.CharField(max_length=255, verbose_name='Разрешение экрана')
    accum_volume = models.CharField(max_length=255, verbose_name='Объем батареи')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    sd = models.BooleanField(default=True, verbose_name='Наличие SD карты')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процессора')
    sd_volume_max = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Максимальный объем встраивамой памяти'
    )
    main_cam_mp = models.CharField(max_length=255, verbose_name='Главная камера')
    

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Television(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Диагональ экрана')
    display_type = models.CharField(max_length=255, verbose_name='Тип телевизора')
    matrix_type = models.CharField(max_length=255, verbose_name='Тип матрицы')
    resolution = models.CharField(max_length=255, verbose_name='Разрешение экрана')
    light = models.CharField(max_length=255, verbose_name='Тип подсветки')
    razv = models.CharField(max_length=255, verbose_name='Частота развёртки экрана')
    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Audio(Product):

    type_of_type = models.CharField(max_length=255, verbose_name='Тип')
    power_of_satelit = models.CharField(max_length=255, verbose_name='Выходная мощность сателлитов')
    power = models.CharField(max_length=255, verbose_name='Выходная мощность')
    bluetooth = models.CharField(max_length=255, verbose_name='Bluetooth')
    diametr_of_sab = models.CharField(max_length=255, verbose_name='Диаметр динамика сабвуфера')
    

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Photographic(Product):

    photo_type = models.CharField(max_length=255, verbose_name='Тип фотокамеры')
    matrix_resolution = models.CharField(max_length=255, verbose_name='Разрешение матрицы')
    size_of_matrix = models.CharField(max_length=255, verbose_name='Размер матрицы')
    type_of_matrix = models.CharField(max_length=255, verbose_name='Тип матрицы')
    light = models.CharField(max_length=255, verbose_name='Максимальная светочувствительность')
    zoom = models.CharField(max_length=255, verbose_name='Оптический зум')
    focus_distans = models.CharField(max_length=255, verbose_name='Фокусное расстояние')
    count_of_to = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Количество точек автофокуса'
    )
    format_of_s = models.CharField(max_length=255, verbose_name='Форматы съемки')
    mikrofon = models.CharField(max_length=255, verbose_name='Микрофон')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Office(Product):

    tecnology = models.CharField(max_length=255, verbose_name='Технология печати')
    pechat = models.CharField(max_length=255, verbose_name='Печать')
    resolution = models.CharField(max_length=255, verbose_name='Макс разрешение печати dpi')
    colors = models.CharField(max_length=255, verbose_name='Количество цветов печати')
    wi_fi = models.CharField(max_length=255, verbose_name='Wi-Fi')
    garantiya = models.CharField(max_length=255, verbose_name='Гарантийный срок')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Appliances(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Вид уборки')
    display_type = models.CharField(max_length=255, verbose_name='Тип пылесборника')
    resolution = models.CharField(max_length=255, verbose_name='Потребляемая мощность Вт')
    accum_volume = models.CharField(max_length=255, verbose_name='Выпускной фильтр')
    ram = models.CharField(max_length=255, verbose_name='Объём пылесборника')
    sd = models.CharField(max_length=255, verbose_name='Длина шнура')
    

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Software(Product):

    country = models.CharField(max_length=255, verbose_name='Страна производитель')
    lang = models.CharField(max_length=255, verbose_name='Язык интерфейса')
    product = models.CharField(max_length=255, verbose_name='Продукт')
    platforma = models.CharField(max_length=255, verbose_name='Платформа')
    num_of_user = models.CharField(max_length=255, verbose_name='Количество пользователей')
    type_of_user = models.CharField(max_length=255, verbose_name='Тип пользователя')
    
    

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказ',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Тип заказа',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)
