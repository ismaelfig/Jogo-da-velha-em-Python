from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class JogoDaVelha(GridLayout):
    def __init__(self, **kwargs):
        super(JogoDaVelha, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        self.size = (300, 300)
        self.jogador = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.pontuacao_x = 0
        self.pontuacao_o = 0

        # Rótulos para exibir a pontuação
        self.rotulo_pontuacao_x = Label(text="Pontuação X: 0")
        self.rotulo_pontuacao_o = Label(text="Pontuação O: 0")
        self.add_widget(self.rotulo_pontuacao_x)
        self.add_widget(self.rotulo_pontuacao_o)

        grid_botoes = GridLayout(cols=3, rows=3, spacing=5)

        for i in range(3):
            for j in range(3):
                botao = Button(text="", font_size=20,
                               on_press=lambda instance, row=i, col=j: self.clique(instance, row, col))
                grid_botoes.add_widget(botao)

        self.add_widget(grid_botoes)

    def clique(self, instance, row, col):
        if self.tabuleiro[row][col] == "":
            self.tabuleiro[row][col] = self.jogador
            instance.text = self.jogador
            instance.disabled = True
            if self.verificar_vitoria():
                self.mostrar_popup(f"O jogador {self.jogador} venceu!")
                self.atualizar_pontuacao()
                self.reiniciar_jogo()
            elif self.verificar_empate():
                self.mostrar_popup("O jogo terminou em empate!")
                self.reiniciar_jogo()
            else:
                self.jogador = "O" if self.jogador == "X" else "X"

    def verificar_vitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != "":
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != "":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != "":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != "":
            return True
        return False

    def verificar_empate(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == "":
                    return False
        return True

    def mostrar_popup(self, mensagem):
        popup = Popup(title='Fim do jogo', content=Label(text=mensagem), size_hint=(None, None), size=(400, 200))
        popup.open()

    def atualizar_pontuacao(self):
        if self.jogador == "X":
            self.pontuacao_x += 1
        else:
            self.pontuacao_o += 1

        self.rotulo_pontuacao_x.text = f"Pontuação X: {self.pontuacao_x}"
        self.rotulo_pontuacao_o.text = f"Pontuação O: {self.pontuacao_o}"

    def reiniciar_jogo(self):
        for child in self.children:
            if isinstance(child, GridLayout):
                for button in child.children:
                    if isinstance(button, Button):
                        button.text = ""
                        button.disabled = False
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = ""
        self.jogador = "X"


class JogoApp(App):
    def build(self):
        return JogoDaVelha()


if __name__ == '__main__':
    JogoApp().run()
