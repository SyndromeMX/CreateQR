import qrcode
from PIL import Image, ImageDraw

def generate_qr_with_logo(url, logo_path, output_path='qr_code.png'):
    # Создаем QR-код
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Создаем изображение QR-кода
    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')
    
    # Открываем логотип
    logo = Image.open(logo_path)
    
    # Создаем белый фон для логотипа
    logo_size = qr_img.size[0] // 4
    white_bg = Image.new('RGB', (logo_size, logo_size), 'white')
    logo = logo.resize((logo_size, logo_size))
    
    # Накладываем логотип на белый фон
    white_bg.paste(logo, (0, 0), mask=logo if logo.mode == 'RGBA' else None)
    
    # Определяем координаты центра
    pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
    
    # Вставляем логотип
    qr_img.paste(white_bg, pos)
    
    # Сохраняем результат
    qr_img.save(output_path)
    print(f'QR-код сохранен как {output_path}')

# Пример использования
url = 'https://example.com'
logo_path = 'logo.png'  # Замените на путь к вашему логотипу
generate_qr_with_logo(url, logo_path)
