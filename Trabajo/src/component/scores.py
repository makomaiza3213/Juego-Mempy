from src.handlers.scores import new_lists_with_corresponding_scores
from src.windows import layout_scores


def score_table():
    """
        visualización del tablero de puntajes de todos los jugadores en todos los niveles con su maxima puntuación
    """
    scores_lists = new_lists_with_corresponding_scores()

    window = layout_scores.table_scores(scores_lists[0], scores_lists[1], scores_lists[2], scores_lists[3])

    event, values = window.read()

    if event in "VOLVER AL MENÚ":
        window.close()


def start():
    """
        Ejecución de la ventana de puntuaciones
    """
    score_table()
