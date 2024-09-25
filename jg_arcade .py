import arcade
import random

largura_tela=900
altura_tela=700
titulo_tela=("Jogo Rhawan Arcade")

quadrado_tamanho= 50
quadrado_cor= arcade.color.RED_VIOLET
quadrado_velocidade= 20

estrela_tamanho=30
estrela_cor= arcade.color.YELLOW

class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(largura_tela,altura_tela,)

        self.quadrado_x= largura_tela//2
        self.quadrado_y= altura_tela//2
        self.estrela_x=random.randint(estrela_tamanho, largura_tela - estrela_tamanho)
        self.estrela_y=random.randint(estrela_tamanho, largura_tela - estrela_tamanho)
        self.pontuacao=0
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.quadrado_x, self.quadrado_y,quadrado_tamanho, quadrado_tamanho, quadrado_cor)
        arcade.draw_rectangle_filled(self.estrela_x,self.estrela_y,estrela_tamanho, estrela_tamanho, estrela_cor)
        arcade.draw_text(f"pontuação:{self.pontuacao}",10,altura_tela-20, arcade.color.WHITE,14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.quadrado_x -= quadrado_velocidade
        elif key == arcade.key.UP:
            self.quadrado_y += quadrado_velocidade
        elif key == arcade.key.RIGHT:
            self.quadrado_x += quadrado_velocidade
        elif key == arcade.key.DOWN:
            self.quadrado_y -= quadrado_velocidade     
    
        self.checar_colisao()
    
    def checar_colisao(self):
        if (self.quadrado_x - quadrado_tamanho // 2 < self.estrela_x + estrela_tamanho // 2 and
                self.quadrado_x + quadrado_tamanho // 2 > self.estrela_x - estrela_tamanho // 2 and
                self.quadrado_y - quadrado_tamanho // 2 < self.estrela_y + estrela_tamanho // 2 and
                self.quadrado_y + quadrado_tamanho // 2 > self.estrela_y - estrela_tamanho // 2):
            self.pontuacao += 1
            self.estrela_x = random.randint(estrela_tamanho, largura_tela - estrela_tamanho)
            self.estrela_y = random.randint(estrela_tamanho, altura_tela - estrela_tamanho)

def main():
    jogo = Jogo()
    arcade.run()

if __name__ == "__main__":
    main()
