from PIL import Image


def get_coordinates(w, h):
    return int(w / 2), int(h / 2)


if __name__ == '__main__':
    img = Image.open('cave.jpg')
    width, height = img.size

    even = Image.new('RGB', get_coordinates(width, height))
    odd = Image.new('RGB', get_coordinates(width, height))

    for i in range(width):
        for j in range(height):
            pixel = img.getpixel((i, j))
            if (i + j) % 2 == 0:
                even.putpixel(get_coordinates(i, j), pixel)
            else:
                odd.putpixel(get_coordinates(i, j), pixel)

    even.save('e.jpg')
    odd.save('o.jpg')
