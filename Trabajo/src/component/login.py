from src.component import new_user, menu_game, class_player
from src.handlers import sounds
from src.handlers.login import functionalities_enter
from src.windows import layout_sign_in as layout


def loop():
    """
        capta los eventos y los valores de entrada para su procesamiento y posterior redirigido correcto
    """
    window = layout.login()

    sounds.play_sound('game music.wav')
    event, values = window.read()
    # keyboard.on_press_key("Intro", functionalities_enter(window, values))

    if event == "ENTRAR":
        functionalities_enter(window, values)

    if event == "REGISTRATE":
        sounds.play_sound('click.wav')
        window.close()
        new_user.start()

    if event == " SALIR ":
        window.close()


def start():
    """
        Lanza la ejecución de la ventana del menú de inicio de sesión y registro
    """
    loop()
