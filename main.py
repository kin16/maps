import pygame
import requests

class Map:
    def __init__(self):
        self.lat = 48.1501781
        self.lon = 11.5106525
        self.size = "600,400"
        self.z = "10"

    def coords(self):
        return f"{self.lon},{self.lat}"

def download(parametrs):
    request = f"https://static-maps.yandex.ru/1.x/?ll={parametrs[0]}&size={parametrs[1]}&l=map&z={parametrs[2]}"
    print(request)
    response = requests.get(request)

    image = "map.png"
    with open(image, 'wb') as file:
        file.write(response.content)
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Maps')
    screen = pygame.display.set_mode((600, 400))

    map = Map()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(pygame.image.load(download([map.coords(), map.size, map.z])), (0, 0))
        pygame.display.flip()
    pygame.quit()