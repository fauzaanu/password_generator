import flet
from flet import Page, TextField, ElevatedButton, Row, Container
import random


def main(page: Page):
    def generate(e):

        # nord vpn blog says these are best:
        # #
        # X5j13$  # eCM1cG@Kdc
        # % j8kr ^ Zfpr!Kf  # ZjnGb$
        # PkxgbEM % @ hdBnub4T
        # vUUN7E @!2
        # v5TtJSyZ

        list_of_cool_chars = ["!", "@", "#", "$", "^", "!", "%"]
        list_to_be_used = []
        phrase = textbox.value
        length = 10  # later we can add a way for user to decide it...

        for i in range(length):
            list_to_be_used.append(random.choice(list_of_cool_chars))

        for char in list_to_be_used:
            phrase = phrase + char

        if len(textbox.value) >= length:
            textbox.value = ""
            button.text = "GENERATE PASSWORD"
            page.update()

        elif textbox.value != "":
            textbox.value = phrase
            button.text = "Clear"
            page.update()

    page.theme_mode = "light"
    # user enters a keyword that he will remember
    # we add random symbols to it and output it

    # GUI planning
    # a text box and a button only
    # text gets replaced

    # inspired by: https://github.com/florinpop17/app-ideas
    # and because im very bored today

    textbox = TextField(label="Enter a phrase")
    button = ElevatedButton(text="GENERATE PASSWORD", on_click=generate)

    row = Row(controls=[textbox, button], alignment="center")
    row_contain = Container(content=row, padding=page.height / 2)
    page.add(row_contain)


flet.app(target=main)
