from setting import*

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def draw(self, targer_pos):
        self.offset.x = -(targer_pos[0] - WINDOW_WIDTH/2)
        self.offset.y = -(targer_pos[1] - WINDOW_HEIGHT/2)
        for sprites in self:
            self.display_surface.blit(sprites.image,sprites.rect.topleft + self.offset)