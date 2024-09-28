
from colorama import Fore, Back, Style
print(Fore.RED + 'ЧЕРВОНИЙ ТЕКСТ')
print(Back.WHITE + 'білий задній фон і червоний текст')
print(Style.RESET_ALL)
print(Style.BRIGHT + 'BRIGHT стиль тексту')
print(Style.NORMAL + "NORMAL стиль тексту")
print(Style.DIM + "DIM стиль тексту")
print(Style.RESET_ALL)
print('звичайний текст')

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print("colorama дозволяє виводити текст" + Fore.BLUE + " різним кольором (Fore)," + Style.BRIGHT + "шрифтом (Style) і " + Back.YELLOW + "заднім фоном (Back)." + Style.RESET_ALL)