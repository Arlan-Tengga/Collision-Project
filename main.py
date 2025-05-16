from setting import*
from player import player
from sprites import*
from Groups import AllSprites
from random import randint
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Project')
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.setup()
        
                
    def setup(self):
        maps = load_pygame(join('graphics','maps.tmx'))
        for x,y,image in maps.get_layer_by_name('Layer').tiles():
            sprites((x*TILE_SIZE,y*TILE_SIZE),image,self.all_sprites)
        for obj in maps.get_layer_by_name('object'):
            collisionsprites((obj.x,obj.y),pygame.Surface((obj.width,obj.height)),self.collision_sprites)
        for obj in maps.get_layer_by_name('Etenise'):
            if obj.name == "player":
                self.player = player((obj.x,obj.y),self.all_sprites,self.collision_sprites)        
                
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update(dt)

            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()