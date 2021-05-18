from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge'
    },
    'desktop': {
        'Модель Процессора': 'model_proc',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Блок питания': 'block_pitania'
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Разрешение экрана': 'resolution',
        'Заряд аккумулятора': 'accum_volume',
        'Оперативная память': 'ram',
        'Наличие слота для SD карты': 'sd',
        'Максимальный объем SD карты': 'sd_volume_max',
        'Камера (МП)': 'main_cam_mp',
        'Фронтальная камера (МП)': 'frontal_cam_mp',
        'Частота процессора': 'processor_freq'
    },
    'tablet': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Разрешение экрана': 'resolution',
        'Заряд аккумулятора': 'accum_volume',
        'Оперативная память': 'ram',
        'Наличие слота для SD карты': 'sd',
        'Максимальный объем SD карты': 'sd_volume_max',
        'Камера (МП)': 'main_cam_mp',
        'Частота процессора': 'processor_freq'
    },
    'television': {
        'Диагональ экрана': 'diagonal',
        'Тип телевизора': 'display_type',
        'Разрешение экрана': 'resolution',
        'Тип матрицы': 'matrix_type',
        'Тип подсветки':'light',
        'Частота развёртки экрана':'razv'
    },
    'audio': {
        'Тип': 'type_of_type',
        'Выходная мощность сателлитов': 'power_of_satelit',
        'Выходная мощность': 'power',
        'Bluetooth': 'bluetooth',
        'Диаметр динамика сабвуфера': 'diametr_of_sab'
        
    },
    'photographic': {
        'Тип фотокамеры': 'photo_type',
        'Разрешение матрицы': 'matrix_resolution',
        'Размер матрицы': 'size_of_matrix',
        'Тип матрицы': 'type_of_matrix',
        'Максимальная светочувствительность': 'light',
        'Оптический зум': 'zoom',
        'Фокусное расстояние': 'focus_distans',
        'Количество точек автофокуса': 'count_of_to',
        'Форматы съемки': 'format_of_s',
        'Микрофон': 'mikrofon'
    },
    'office': {
        'Технология печати': 'tecnology',
        'Печать': 'pechat',
        'Макс разрешение печати dpi': 'resolution',
        'Количество цветов печати': 'colors',
        'Wi-Fi': 'wi_fi',
        'Гарантийный срок': 'garantiya',
        'Вес': 'weight'
       
    },
    'appliances': {
        'Вид уборки': 'diagonal',
        'Тип пылесборника': 'display_type',
        'Потребляемая мощность Вт': 'resolution',
        'Выпускной фильтр': 'accum_volume',
        'Объём пылесборника': 'ram',
        'Длина шнура': 'sd'
        
    },
    'software': {
        'Страна производитель': 'country',
        'Язык интерфейса': 'lang',
        'Продукт': 'product',
        'Платформа': 'platforma',
        'Количество пользователей': 'num_of_user',
        'Тип пользователя': 'type_of_user'
       
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Максимальный объем SD карты', None)
        else:
            PRODUCT_SPEC['smartphone']['Максимальный объем SD карты'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

