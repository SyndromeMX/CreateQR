import qrcode
from PIL import Image, ImageDraw, ImageFilter

def generate_qr_with_rounded_corners(url, logo_path, output_path='qr_code.png', corner_radius=30):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

    logo = Image.open(logo_path)
    
   
    logo_size = qr_img.size[0] // 4
    white_bg = Image.new('RGB', (logo_size, logo_size), 'white')
    logo = logo.resize((logo_size, logo_size))
    
    white_bg.paste(logo, (0, 0), mask=logo if logo.mode == 'RGBA' else None)
    
    pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
    
    qr_img.paste(white_bg, pos)

    # Создаем маску для скругленных углов
    mask = Image.new("L", qr_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, qr_img.size[0], qr_img.size[1]), corner_radius, fill=255)
    qr_img = qr_img.convert("RGBA")
    qr_img.putalpha(mask)
    qr_img.save(output_path)
    print(f'QR-код сохранен как {output_path}')

url = 'https://github.com/SyndromeMX'
logo_path = 'logo.png'  
generate_qr_with_rounded_corners(url, logo_path)
