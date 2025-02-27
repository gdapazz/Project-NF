from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
import random
from noticias import noticias_lista 

class NoticiaSeguraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.titulo = Label(
            text="Notícia Segura",
            font_size=32,
            bold=True,
            size_hint_y=None,
            height=260
        )

        
        self.logo = Image(
    source="imagens/Logo.png",
    size_hint=(None, None),  
    size=(200, 200),  
    pos_hint= {'center_x': 0.5, 'y': 0.5}  
)

        self.texto_intro = """Vivemos em uma era em que as informações circulam com uma velocidade impressionante. 
        No entanto, nem todas as notícias que recebemos são verdadeiras. Para combater a desinformação, 
        criamos o Notícia Segura, um aplicativo desenvolvido especialmente para ajudá-lo a identificar fontes confiáveis, 
        verificar a veracidade das informações e evitar cair em fake news. 
        Utilizando dados de fontes seguras e verificadas, o Notícia Segura é seu aliado 
        na busca por uma informação precisa e confiável..

A informação correta é um direito de todos."""

        self.texto_label = Label(
            text=self.texto_intro,
            font_size=23,
            halign="center",
            valign="bottom",
            size_hint_y=None
        )
        self.texto_label.bind(size=lambda instance, value: setattr(instance, 'text_size', (value[0], None)))

        self.botao_iniciar = Button(text="Iniciar", size_hint=(None, None), size=(200, 50))
        self.botao_sair = Button(text="Sair", size_hint=(None, None), size=(200, 50))
        self.botao_sair.bind(on_press=self.fechar_app)
        self.botao_iniciar.bind(on_press=self.mostrar_nome_idade)

        self.layout.add_widget(self.titulo)
        self.layout.add_widget(self.logo)  
        self.layout.add_widget(self.texto_label)
        self.layout.add_widget(self.botao_iniciar)
        self.layout.add_widget(self.botao_sair)

        self.noticias_exibidas = []  

        return self.layout

    def fechar_app(self, instance):
        App.get_running_app().stop()

    def mostrar_nome_idade(self, instance):
        self.layout.clear_widgets()
        
        
        nome_label = Label(text="Qual seu nome?", font_size=23)
        self.nome_input = TextInput(font_size=18, size_hint_y=None, height=40)
        
        idade_label = Label(text="Qual sua idade?", font_size=23)
        self.idade_input = TextInput(font_size=18, size_hint_y=None, height=40)

        botao_salvar = Button(text="Salvar", size_hint=(None, None), size=(200, 50))
        botao_salvar.bind(on_press=self.salvar_dados)

    
        self.layout.add_widget(nome_label)
        self.layout.add_widget(self.nome_input)
        self.layout.add_widget(idade_label)
        self.layout.add_widget(self.idade_input)
        self.layout.add_widget(botao_salvar)

    def salvar_dados(self, instance):
        nome = self.nome_input.text
        idade = self.idade_input.text
        print(f"Nome: {nome}, Idade: {idade}")

        self.layout.clear_widgets()
        confirmacao_label = Label(text=f"Bem-vindo, {nome}! Estamos prontos para começar.", font_size=28)
        
        botao_seguir = Button(text="Seguir", size_hint=(None, None), size=(200, 50))
        botao_seguir.bind(on_press=self.mostrar_dicas)

        self.layout.add_widget(confirmacao_label)
        self.layout.add_widget(botao_seguir)

    def mostrar_dicas(self, instance):
        self.layout.clear_widgets()

        texto_dicas = """
        
        
        Fake news são formas de desinformação estrategicamente disseminadas que ganharam impulso graças à internet.
        Com a revolução digital, houve um grande aumento da disseminação de notícias falsas (fake news). Para que esses conteúdos atinjam grande público, são usados algoritmos que aumentam seu alcance e repercussão. Além disso, as notícias falsas são compartilhadas com e por pessoas que já acreditam em determinadas ideias, o que torna ainda maior a chance de produzirem posicionamentos radicais entre as pessoas.
        
        Veja abaixo como identificar fake news:

Chamativas ou bombásticas
Em muitos casos, o título não se relaciona ao restante do texto. Nunca leia só o título e confira se o fato já foi publicado em outros veículos. 

Erros ortográficos ou gramaticais
Textos jornalísticos são revisados antes de serem publicados. Se o texto contém erros, desconfie. Cheque a informação em outros veículos mais reconhecidos.

Textos opinativos como se fossem notícia
Todo artigo opinativo deve vir assinado pelo seu autor. Mesmo em entrevistas, a opinião dos entrevistados é apresentada de forma imparcial pelo veículo. Se a suposta notícia traz opinião disfarçada no meio do texto, não é isenta.

Canais desconhecidos
Convém checar se outros veículos também publicaram a notícia. Isso ajuda a garantir a credibilidade da informação.

Notícia verdadeira mas antiga
Nem sempre as notícias são falsas, mas podem ser antigas e estar descontextualizadas visando gerar desinformação. Por essa razão é importante verificar a data da publicação e buscar a fonte para saber da veracidade do fato e em que data ocorreu.

Fonte:   https://www.tre-pr.jus.br/comunicacao/noticias/2023/Setembro/como-identificar-fake-news-na-duvida-nao-compartilhe-1



"""

        texto_label = Label(
            text=texto_dicas,
            font_size=28,
            size_hint_y=None,
            height=1000,
            halign="center",
            valign="middle",
            text_size=(self.layout.width - 40, None)
        )

        scroll = ScrollView(size_hint=(1, None), size=(self.layout.width, 500))
        scroll.add_widget(texto_label)
        self.layout.add_widget(scroll)

        botao_seguir = Button(text="Seguir", size_hint=(None, None), size=(200, 50))
        botao_seguir.bind(on_press=self.mostrar_proxima_pagina)

        self.layout.add_widget(botao_seguir)

    def mostrar_proxima_pagina(self, instance):
        self.layout.clear_widgets()
        
        texto_conhecimento = """Agora é hora de colocar seu conhecimento à prova! 
        Leia atentamente a notícia e descubra o motivo pelo qual ela é falsa. 
        Preste atenção aos detalhes para identificar os sinais de desinformação. 
        Vamos testar sua habilidade em reconhecer informações confiáveis!

        Os motivos podem ser: Chamativas ou bombásticas, Erros ortográficos ou gramaticais, Textos opinativos, Canais desconhecidos, ou Verdadeiras mas antigas.

        Você está pronto?"""

        texto_label = Label(
            text=texto_conhecimento,
            font_size=34,
            size_hint_y=None,
            height=800,
            halign="center",
            valign="top",
            text_size=(self.layout.width - 40, None)
        )

        botao_estou = Button(text="Estou Pronto.", size_hint=(None, None), size=(200, 50))
        botao_estou.bind(on_press=self.iniciar_testes)

        self.layout.add_widget(texto_label)
        self.layout.add_widget(botao_estou)

    def iniciar_testes(self, instance):
        self.acertos = 0
        self.rodadas = 0
        self.mostrar_noticia()
        self.nome = self.nome_input.text  
        self.idade = self.idade_input.text  


    def mostrar_noticia(self):
        if self.rodadas < 5:
            
            if len(self.noticias_exibidas) < len(noticias_lista):
                noticia = random.choice([n for n in noticias_lista if n not in self.noticias_exibidas])  
                self.noticias_exibidas.append(noticia)  
            else:
                noticia = random.choice(noticias_lista)  

            noticia_titulo = noticia["titulo"]
            noticia_texto = noticia["texto"]
            self.motivo_correto = noticia["motivo"]
            self.imagem = noticia["imagem"]

            self.layout.clear_widgets()

            titulo_label = Label(text=noticia_titulo, font_size=22, bold=True)
            imagem_label = Image(source=self.imagem)
            noticia_label = Label(text=noticia_texto, font_size=18)
            motivo_input = TextInput(hint_text="Chamativas ou bombásticas, Erros ortográficos ou gramaticais, Textos opinativos, Canais desconhecidos, Verdadeiras mas antigas.", font_size=16, size_hint_y=None, height=40)
            botao_resposta = Button(text="Responder", size_hint=(None, None), size=(200, 50))
            botao_resposta.bind(on_press=lambda instance: self.verificar_resposta(motivo_input.text))

            self.layout.add_widget(titulo_label)
            self.layout.add_widget(imagem_label)
            self.layout.add_widget(noticia_label)
            self.layout.add_widget(motivo_input)
            self.layout.add_widget(botao_resposta)
        else:
            self.layout.clear_widgets()
            resultado_label = Label(text=f"Você acertou {self.acertos} de 5 notícias.", font_size=28)


            with open("Ranking.txt", "a") as f:
             f.write(f"Nome: {self.nome}. Idade: {self.idade}. Acertos: {self.acertos}.\n")

             botao_ranking = Button(text="Ver ranking", size_hint=(None, None), size=(200, 50))
            botao_ranking.bind(on_press=self.mostrar_ranking)

            self.layout.add_widget(resultado_label)
            self.layout.add_widget(botao_ranking)


    def verificar_resposta(self, resposta):
        if resposta.lower() == self.motivo_correto.lower():
            self.acertos += 1
        self.rodadas += 1
        self.mostrar_noticia()
    def mostrar_ranking(self, instance):
        self.layout.clear_widgets()

        ranking_label = Label(text="Ranking de Usuários", font_size=30, bold=True)
        self.layout.add_widget(ranking_label)

        try:
            with open("Ranking.txt", "r") as file:
                ranking_texto = file.read()
        except FileNotFoundError:
            ranking_texto = "Nenhum ranking disponível."

        ranking_conteudo = Label(text=ranking_texto, font_size=18)
        self.layout.add_widget(ranking_conteudo)


    

    
     

if __name__ == "__main__":
    NoticiaSeguraApp().run()