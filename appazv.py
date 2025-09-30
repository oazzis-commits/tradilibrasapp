# tem q importar o app, builder (gui)
# criar o app
# criar a função build
# link = coloca o link. :pra ter variavel no link coloca {}
# requisicao = requests.get(link) :permite receber a inf, tem q por no import antes

#configuracoes no .kv:
#Item:
#configuracoes: valor
#Label = texto
#button = botao

from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from functools import partial
from random import sample
import json, os



perguntas = [
    {
        "parte": "aleatorio",
        "texto": "Essa é a letra 'A'?",
        "alternativas": ["Sim", "Não"],
        "correta": "Sim",
        "video": "videos/videoa.mp4"
    },
    {
        "parte": "aleatorio",
        "texto": "Que letra é essa?",
        "alternativas": ["G", "N", "A", "M"],
        "correta": "G",
        "video": "videos/videog.mp4"
    },
    {
        "parte": "aleatorio",
        "texto": "Que letra é essa?",
        "alternativas": ["G", "N", "A", "M"],
        "correta": "N",
        "video": "videos/videon.mp4"
    },
{
        "parte": "aleatorio",
        "texto": "Que letra é essa?",
        "alternativas": ["G", "N", "A", "M"],
        "correta": "A",
        "video": "videos/videoa.mp4"
    },
{
        "parte": "aleatorio",
        "texto": "Essa é a letra 'S'?",
        "alternativas": ["Sim", "Não"],
        "correta": "Não",
        "video": "videos/videon.mp4"
    },
{
        "parte": "aleatorio",
        "texto": "Esse é o sinal de 'bom dia' em Libras?",
        "alternativas": ["Sim", "Não"],
        "correta": "Sim",
        "video": "videos/videobomdia.mp4"
    },

{
        "parte": "aleatorio",
        "texto": "Que sinal é esse?",
        "alternativas": ["Tudo bem", "Oi", "Obrigado", "Boa noite"],
        "correta": "Tudo bem",
        "video": "videos/videotudobem.mp4"
    },
{
        "parte": "aleatorio",
        "texto": "Esse é o sinal de 'boa noite' em Libras?",
        "alternativas": ["Sim", "Não"],
        "correta": "Não",
        "video": "videos/videoboatarde.mp4"
    },
{
        "parte": "aleatorio",
        "texto": "Que sinal é esse?",
        "alternativas": ["Boa Tarde", "Tchau", "Bom Dia", "Boa Noite"],
        "correta": "Boa Tarde",
        "video": "videos/videoboatarde.mp4"
    },
{
        "parte": "aleatorio",
        "texto": "Esse é o sinal de 'oi' em Libras?",
        "alternativas": ["Sim", "Não"],
        "correta": "Sim",
        "video": "videos/videooi.mp4"
    },
    {
        "parte": "alfabeto",
        "texto": "Essa é a letra 'A'?",
        "alternativas": ["Sim", "Não"],
        "correta": "Sim",
        "video": "videos/videoa.mp4"
    },
    {
        "parte": "alfabeto",
        "texto": "Que letra é essa?",
        "alternativas": ["G", "N", "A", "M"],
        "correta": "G",
        "video": "videos/videog.mp4"
    },
    {
        "parte": "alfabeto",
        "texto": "Que letra é essa?",
        "alternativas": ["G", "N", "A", "M"],
        "correta": "N",
        "video": "videos/videon.mp4"
    },
{
        "parte": "alfabeto",
        "texto": "Que letra é essa?",
        "alternativas": ["G", "N", "A", "M"],
        "correta": "A",
        "video": "videos/videoa.mp4"
    },
{
        "parte": "alfabeto",
        "texto": "Essa é a letra 'S'?",
        "alternativas": ["Sim", "Não"],
        "correta": "Não",
        "video": "videos/videon.mp4"
    },

{
        "parte": "saudacoes",
        "texto": "Esse é o sinal de 'bom dia' em Libras?",
        "alternativas": ["Sim", "Não"],
        "correta": "Sim",
        "video": "videos/videobomdia.mp4"
    },

{
        "parte": "saudacoes",
        "texto": "Que sinal é esse?",
        "alternativas": ["Tudo bem", "Oi", "Obrigado", "Boa noite"],
        "correta": "Tudo bem",
        "video": "videos/videotudobem.mp4"
    },
{
        "parte": "saudacoes",
        "texto": "Esse é o sinal de 'boa noite' em Libras?",
        "alternativas": ["Sim", "Não"],
        "correta": "Não",
        "video": "videos/videoboatarde.mp4"
    },
{
        "parte": "saudacoes",
        "texto": "Que sinal é esse?",
        "alternativas": ["Boa Tarde", "Tchau", "Bom Dia", "Boa Noite"],
        "correta": "Boa Tarde",
        "video": "videos/videoboatarde.mp4"
    },
{
        "parte": "saudacoes",
        "texto": "Esse é o sinal de 'oi' em Libras?",
        "alternativas": ["Sim", "Não"],
        "correta": "Sim",
        "video": "videos/videooi.mp4"
    },
]

class MeuLayout(FloatLayout):
    fundo = StringProperty("imagens/fundotudo.png")

class TelaPrincipal(Screen):
    pass

class TelaOqelibras(Screen):
    titoqe = ObjectProperty(None)
    texin = ObjectProperty(None)
    comap = ObjectProperty(None)
    vidau = ObjectProperty(None)
    pass

class TelaAlfabeto(Screen):
    pass

class TelaSaudacoes(Screen):
    pass

class TelaTradutor(Screen):
    def on_enter(self):
        # Quando o usuário entrar nessa tela, inicia o sensor
        usar_sensor()
    pass

class TelaPraticar(Screen):
    pass

class TelaLetra(Screen):
    letra = StringProperty("")
    imagem_letra = StringProperty("")
    video = StringProperty("")

class TelaTextinf(Screen):
    pass

class TelaVidAula(Screen):
    pass

class TelaVideoaula(Screen):
    videoaula = StringProperty("")
    video = StringProperty("")
    pass

class TelaTextos(Screen):
    titulo_texto = StringProperty("")  # armazena o título do texto que vai mostrar

    def on_enter(self):
        if not self.titulo_texto:
            return  # não faz nada se nenhum título foi definido

        caminho_json = os.path.join(os.path.dirname(__file__), "textos/texto.json")
        with open(caminho_json, "r", encoding="utf-8") as f:
            dados = json.load(f)

        # procura o texto pelo título
        texto_escolhido = next((t for t in dados if t["titulo"] == self.titulo_texto), None)
        if texto_escolhido:
            self.ids.label_texto.text = (
                f"[size=28][b][color=#000000]{texto_escolhido.get('titulo', '')}[/b][/size]\n\n"
                f"[size=20][color=#000000]{texto_escolhido.get('conteudo', '')}[/color][/size]"
            )
        else:
            self.ids.label_texto.text = "Texto não encontrado."

    pass

class TelaCumprimento(Screen):
    cumprimento = StringProperty("")
    imagem_cumprimento = StringProperty("")
    video = StringProperty("")
    pass

class TelaPergunta(Screen):
    perguntas_lista = []
    indice = 0
    acertos = 0
    erros = 0
    dialog = None
    mostrar_correta = False

    def on_enter(self):
        if not self.perguntas_lista:
            self.carregar_perguntas("saudacoes")  # ou "saudacoes", dependendo do tema

    def carregar_perguntas(self, parte):
        from random import shuffle

        todas_perguntas = [p for p in perguntas if p["parte"] == parte]
        if not todas_perguntas:
            self.ids.pergunta_texto.text = "Nenhuma pergunta disponível."
            self.ids.video_pergunta.source = ""
            self.ids.video_pergunta.state = "stop"
            return


        shuffle(todas_perguntas)  # embaralha as perguntas
        self.perguntas_lista = todas_perguntas[:5]  # pega as primeiras 5 perguntas
        self.indice = 0
        self.acertos = 0
        self.erros = 0
        self.mostrar_pergunta()  # atualiza a tela

    def mostrar_pergunta(self):
        box = self.ids.alternativas_box
        box.clear_widgets()

        if self.indice >= len(self.perguntas_lista):
            self.ids.pergunta_texto.text = f"Fim das perguntas!\nAcertos: {self.acertos}\nErros: {self.erros}"
            self.ids.video_pergunta.source = ""
            return

        pergunta = self.perguntas_lista[self.indice]
        self.ids.pergunta_texto.text = pergunta["texto"]

        # Tenta carregar o vídeo, mas não trava se der erro
        video_path = pergunta.get("video", "")
        if video_path:
            try:
                # Caminho absoluto seguro
                video_path_abs = os.path.join(os.path.dirname(__file__), video_path)
                if os.path.exists(video_path_abs):
                    self.ids.video_pergunta.source = video_path_abs
                    self.ids.video_pergunta.state = "stop"
                    self.ids.video_pergunta.state = "play"
                else:
                    print(f"[AVISO] Vídeo não encontrado: {video_path_abs}")
                    self.ids.video_pergunta.source = ""
            except Exception as e:
                print(f"[ERRO] Não foi possível carregar o vídeo: {video_path_abs}\n{e}")
                self.ids.video_pergunta.source = ""
        else:
            self.ids.video_pergunta.source = ""

        for alt in pergunta["alternativas"]:
            btn = MDRaisedButton(
                text=alt,
                on_release=partial(self.verificar_resposta, alt)
            )
            box.add_widget(btn)

    def verificar_resposta(self, resposta, btn):

        correta = self.perguntas_lista[self.indice]["correta"]

        for child in self.ids.alternativas_box.children:
            child.disabled = True

        if resposta == correta:
            self.acertos += 1
            texto_dialogo = "Resposta correta!"
            botoes = [MDFlatButton(text="OK", on_release=self.proxima_com_dialog)]
            self.mostrar_correta = False
        else:
            self.erros += 1
            texto_dialogo = "Resposta incorreta!"
            botoes = [
                MDFlatButton(text="Refazer", on_release=self.refazer_pergunta),
                MDFlatButton(text="Próxima", on_release=self.proxima_com_dialog)
            ]
            self.mostrar_correta = True

        self.dialog = MDDialog(text=texto_dialogo, buttons=botoes)
        self.dialog.open()

    def refazer_pergunta(self, *args):
        self.dialog.dismiss()
        self.mostrar_pergunta()

    def proxima_com_dialog(self, *args):
        self.dialog.dismiss()
        if self.mostrar_correta:
            correta = self.perguntas_lista[self.indice]["correta"]
            self.ids.pergunta_texto.text = f"A resposta correta era: {correta}"
            Clock.schedule_once(lambda dt: self.avancar_pergunta(), 1.5)
        else:
            self.avancar_pergunta()

    def avancar_pergunta(self):
        self.indice += 1
        self.mostrar_pergunta()
    pass

class TelaRelatorio(Screen):
    pass

class Gerenciador(ScreenManager):
    pass
sm = Gerenciador()
sm.add_widget(TelaLetra(name="tela_letra"))

GUI = Builder.load_file("telaapp.kv")
Builder.load_file("templatealfabetos.kv")
Builder.load_file("telatextinf.kv")
Builder.load_file("telavidaula.kv")
Builder.load_file("praticar.kv")
Builder.load_file("templatesaudacoes.kv")

class Tradilibras(MDApp):

    def build(self):
    # parte padrao pra criar qualquer codigo
        layout = MeuLayout()
        Clock.schedule_once(lambda dt: self.trocar_cor(layout), 1)
        self.sm = ScreenManager()

        self.sm.add_widget(TelaPrincipal(name='principal'))
        self.sm.add_widget(TelaOqelibras(name='oqelibras'))
        self.sm.add_widget(TelaAlfabeto(name='alfabeto'))
        self.sm.add_widget(TelaSaudacoes(name='saudacoes'))
        self.sm.add_widget(TelaTradutor(name='tradutor'))
        self.sm.add_widget(TelaPraticar(name='praticar'))
        self.sm.add_widget(TelaLetra(name='tela_letra'))
        self.sm.add_widget(TelaTextinf(name='tela_textinf'))
        self.sm.add_widget(TelaVidAula(name='tela_vidaula'))
        self.sm.add_widget(TelaPergunta(name='tela_pergunta'))
        self.sm.add_widget(TelaRelatorio(name='tela_relatorio'))
        self.sm.add_widget(TelaVideoaula(name='tela_videoaula'))
        self.sm.add_widget(TelaTextos(name='tela_textos'))
        self.sm.add_widget(TelaCumprimento(name='tela_cumprimento'))
        self.sm.add_widget(SensorScreen(name="sensor"))
        return self.sm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.historico_telas = []

    def mostrar_letra(self, letra):
        tela = self.sm.get_screen("tela_letra")
        tela.letra = letra
        tela.imagem_letra = f"imagens/{letra.lower()}.png"

        video_path = f"videos/video{letra.lower()}.mp4"
        tela.ids.video_letra.source = video_path
        tela.ids.video_letra.state = 'stop'  # para garantir que o vídeo reinicie
        tela.ids.video_letra.state = 'play'  # começa a tocar

        self.mudar_tela("tela_letra")

    def mostrar_videoaula(self, videoaula):
        tela = self.sm.get_screen("tela_videoaula")
        tela.videoaula = videoaula

        video_path = os.path.join(os.path.dirname(__file__), "videos", f"{videoaula.lower()}.mp4")

        if not os.path.exists(video_path):
            print(f"Vídeo não encontrado: {video_path}")
            return

        tela.ids.video_videoaula.source = video_path
        tela.ids.video_videoaula.state = 'stop'
        tela.ids.video_videoaula.state = 'play'

        self.mudar_tela("tela_videoaula")

    def mostrar_texto_especifico(self, titulo):
        tela = self.sm.get_screen("tela_textos")
        tela.titulo_texto = titulo
        self.mudar_tela("tela_textos")

    def mostrar_cumprimento(self, cumprimento):
        tela = self.sm.get_screen("tela_cumprimento")
        tela.cumprimento = cumprimento
        tela.imagem_cumprimento = f"imagens/{cumprimento.lower()}.png"

        video_path = f"videos/video{cumprimento.lower()}.mp4"
        tela.ids.video_cumprimento.source = video_path
        tela.ids.video_cumprimento.state = 'stop'
        tela.ids.video_cumprimento.state = 'play'

        self.mudar_tela("tela_cumprimento")

    def mudar_tela(self, nome):
        if self.sm.current != nome:
            self.historico_telas.append(self.sm.current)
        if not self.sm.has_screen(nome):
            telas = {
                "oqelibras": TelaOqelibras,
                "alfabeto": TelaAlfabeto,
                "saudacoes": TelaSaudacoes,
                "tradutor": TelaTradutor,
                "praticar": TelaPraticar,
                "tela_letra": TelaLetra
            }
            if nome in telas:
                self.sm.add_widget(telas[nome](name=nome))
        self.sm.current = nome  # muda a tela pelo sm

    def voltar_tela(self):
        if self.historico_telas:
            tela_anterior = self.historico_telas.pop()  # pega a última tela
            self.sm.current = tela_anterior

    def botao_clicado(self, widget):
        widget.background_color = [0.741, 0.184, 0.416, 1]  # muda cor
        print(f"Botão clicado: {widget.text}")

    def trocar_cor(self, layout):
        layout.cor_fundo = [1, 0.9, 0.85, 1]

    def on_start(self):
        azulescuro = [0x1A / 255, 0x58 / 255, 0x9C / 255, 1]  # [0.102, 0.345, 0.612, 1]
        azulmedio = [0x58 / 255, 0x86 / 255, 0xBA / 255, 1]  # [0.345, 0.525, 0.729, 1]
        azulclaro = [0xA0 / 255, 0xCA / 255, 0xE0 / 255, 1]  # [0.627, 0.792, 0.878, 1]
        bege = [0xF1 / 255, 0xEC / 255, 0xE6 / 255, 1]  # [0.945, 0.925, 0.902, 1]
        preto = [0, 0, 0, 1]

        tela_principal = self.root.get_screen('principal')

        tela_principal.ids.trad.color = azulescuro
        tela_principal.ids.sin.color = azulescuro
        tela_principal.ids.duv.color = azulescuro
        tela_principal.ids.oqe.color = preto
        tela_principal.ids.alf.color = preto
        tela_principal.ids.sau.color = preto
        tela_principal.ids.tra.color = preto
        tela_principal.ids.pra.color = preto

        tela_praticar = self.root.get_screen('praticar')

        tela_praticar.ids.aleatorio.color = azulescuro
        tela_praticar.ids.alfabeto.color = azulescuro
        tela_praticar.ids.saudacoes.color = azulescuro
        tela_praticar.ids.vampra.color = azulescuro
        tela_praticar.ids.escolhatema.color = azulescuro

        tela_oqelibras = self.root.get_screen('oqelibras')

        tela_oqelibras.ids.titoqe.color = azulescuro
        tela_oqelibras.ids.texin.color = azulescuro
        tela_oqelibras.ids.comap.color = azulescuro
        tela_oqelibras.ids.vidau.color = azulescuro

        tela_textinf = self.root.get_screen('tela_textinf')

        tela_textinf.ids.oqeinf.color = azulescuro
        tela_textinf.ids.titextinf.color = azulescuro
        tela_textinf.ids.texto1.color = azulescuro
        tela_textinf.ids.texto2.color = azulescuro
        tela_textinf.ids.texto3.color = azulescuro
        tela_textinf.ids.texto4.color = azulescuro
        tela_textinf.ids.texto5.color = azulescuro

        tela_vidaula = self.root.get_screen('tela_vidaula')

        tela_vidaula.ids.oqevid.color = azulescuro
        tela_vidaula.ids.titvideoaulas.color = azulescuro

        tela_alfabeto = self.root.get_screen('alfabeto')

        tela_alfabeto.ids.sinalf.color = azulescuro
        tela_alfabeto.ids.sinalfemb.color = azulescuro
        tela_alfabeto.ids.revalf.color = azulescuro
        tela_alfabeto.ids.apralf.color = azulescuro

        tela_saudacoes = self.root.get_screen('saudacoes')

        tela_saudacoes.ids.sinsau.color = azulescuro
        tela_saudacoes.ids.sinsauemb.color = azulescuro
        tela_saudacoes.ids.revsau.color = azulescuro
        tela_saudacoes.ids.aprsau.color = azulescuro
        tela_saudacoes.ids.bomdia.color = azulescuro
        tela_saudacoes.ids.boatarde.color = azulescuro
        tela_saudacoes.ids.boanoite.color = azulescuro
        tela_saudacoes.ids.oi.color = azulescuro
        tela_saudacoes.ids.tudobem.color = azulescuro
        tela_saudacoes.ids.tchau.color = azulescuro

if __name__ == "__main__":
    Tradilibras().run()
