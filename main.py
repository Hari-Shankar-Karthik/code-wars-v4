from engine.main import Game
import scriptblue, scriptred, my_script

if __name__ == "__main__":
    G = Game((40, 40), my_script, scriptblue)
    G.run_game()