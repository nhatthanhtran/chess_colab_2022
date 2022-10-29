from chess.gui.app import ChessApp
from chess.gui.main_window import ChessMainWindow

def main(argv):
    app = ChessApp(argv)
    main_window = ChessMainWindow()
    main_window.show()
    return app.exec()
