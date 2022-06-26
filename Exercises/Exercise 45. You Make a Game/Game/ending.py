from textwrap import dedent
from saving import save

saving_text = save()


class finish:
    
    def restart(function):
        action = input('')

        if action == 'restart':
            return function('home')


    def end(scene, win, restart_function, 
            total_time):

        print(scene)
        total_time_playing = total_time
        saving_text.Switch('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 3, 'home')
        print(dedent(f"""
            You {'win' if win else 'lose'}! you spent {total_time_playing} playing the game.
            press enter to exit or type 'restart' to replay the game.
        """))

        if win:
            current_wins = int(saving_text.GetLine('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 'wins', {}).split()[2])
            saving_text.Switch('C:\\Users\\Nayef\\OneDrive - Ministry of Education\\Documents\\Python\\Learn Python 3 the Hard Way\\Exercise 45. You Make a Game\\ex45 game\\Game\\saving.txt', 5, f"{current_wins + 1}")
        finish.restart(restart_function)