from PIL import Image

def image_to_pixels(image_path):
    """
    Преобразует изображение в набор пикселей.

    :param image_path: путь к изображению
    :return: список пикселей (каждый пиксель представлен в формате RGB)
    """
    try:
        # Открываем изображение
        img = Image.open(image_path)

        # Убедимся, что изображение в формате RGB
        img = img.convert("RGB")

        # Получаем размеры изображения
        width, height = img.size

        # Преобразуем изображение в набор пикселей
        pixels = list(img.getdata())

        # Преобразуем список в двумерный массив, чтобы соотносить координаты
        pixel_matrix = [pixels[i * width:(i + 1) * width] for i in range(height)]

        return pixel_matrix
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{image_path}' не найден. Проверьте путь к файлу.")

def create_pixel_art(image_path, output_path, pixel_size):
    """
    Преобразует изображение в пиксель-арт и сохраняет его.

    :param image_path: путь к входному изображению
    :param output_path: путь для сохранения пиксель-арта
    :param pixel_size: размер одного пикселя в пиксель-арте
    """
    try:
        # Открываем изображение
        img = Image.open(image_path)

        # Убедимся, что изображение в формате RGB
        img = img.convert("RGB")

        # Уменьшаем изображение для создания эффекта пиксель-арта
        small_img = img.resize(
            (img.width // pixel_size, img.height // pixel_size),
            Image.NEAREST
        )

        # Увеличиваем его обратно до исходного размера
        pixel_art = small_img.resize(
            (img.width, img.height),
            Image.NEAREST
        )

        # Сохраняем результат
        pixel_art.save(output_path)
        print(f"Пиксель-арт успешно сохранён в {output_path}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{image_path}' не найден. Проверьте путь к файлу.")
    except Exception as e:
        raise RuntimeError(f"Ошибка создания пиксель-арта: {e}")

def pixels_to_image(pixel_matrix, output_path):
    """
    Создаёт изображение из набора пикселей и сохраняет его.

    :param pixel_matrix: двумерный массив пикселей (каждый пиксель представлен в формате RGB)
    :param output_path: путь для сохранения выходного изображения
    """
    try:
        # Определяем размеры изображения
        height = len(pixel_matrix)
        width = len(pixel_matrix[0])

        # Преобразуем двумерный массив обратно в плоский список
        pixels = [pixel for row in pixel_matrix for pixel in row]

        # Создаём новое изображение
        img = Image.new("RGB", (width, height))
        img.putdata(pixels)

        # Сохраняем изображение
        img.save(output_path, format="PNG")
        print(f"Изображение успешно сохранено в {output_path}")
    except Exception as e:
        raise RuntimeError(f"Ошибка создания изображения: {e}")

# Пример использования
if __name__ == "__main__":
    image_path = r"F:\загрузки с браузера\я.jpg"  # Укажите путь к вашему изображению
    output_path = r"F:\загрузки с браузера\я h.png"  # Укажите путь для сохранения пиксель-арта
    pixel_size = 10  # Укажите размер пикселя для пиксель-арта

    try:
        # Создаём пиксель-арт
        create_pixel_art(image_path, output_path, pixel_size)
    except Exception as e:
        print(e)
