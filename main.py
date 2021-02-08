import pygame
import requests

class Map:
    def __init__(self):
        self.lat = 54.739646
        self.lon = 55.950876
        self.size = "600,400"
        self.zoom = 10

    def up_zoom(self):
        if self.zoom < 17:
            self.zoom += 1

    def down_zoom(self):
        if self.zoom > 0:
            self.zoom -= 1

    def coords(self):
        return f"{self.lon},{self.lat}"

def download(parametrs):
    request = f"https://static-maps.yandex.ru/1.x/?ll={parametrs[0]}&size={parametrs[1]}&l=map&z={parametrs[2]}"
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP:
                    map.up_zoom()
                if event.key == pygame.K_PAGEDOWN:
                    map.down_zoom()
        screen.blit(pygame.image.load(download([map.coords(), map.size, str(map.zoom)])), (0, 0))
        pygame.display.flip()
    pygame.quit()