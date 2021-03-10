import time
import pyautogui
import PIL.ImageGrab


def wait(x):
    minute = 60
    time.sleep(minute*10)  # min * num of minutes


def get_pixel_color(x, y):
    rgb = PIL.ImageGrab.grab().load()[x, y]
    return rgb


def detect_change(x, y, prev_rgb):

    acc_button_x = 1275
    acc_button_y = 944

    while 'Queue':
        rgb = get_pixel_color(x, y)
        if rgb == prev_rgb:
            print(rgb)
        else:
            pyautogui.click(acc_button_x, acc_button_y)
            break
        time.sleep(5)


def play_game():
    time.sleep(2)

    play_button_x = 635
    play_button_y = 298

    tft_button_x = 1255
    tft_button_y = 515

    con_button_x = 1155
    con_button_y = 1107

    lvl_place_x = 1158
    lvl_place_y = 537
    lvl_place_rgb = (5, 8, 9)

    surr_button_x = 1153
    surr_button_y = 652

    pyautogui.click(play_button_x, play_button_y)
    time.sleep(1)
    pyautogui.click(tft_button_x, tft_button_y)
    time.sleep(1)
    pyautogui.click(con_button_x, con_button_y)
    time.sleep(1)
    pyautogui.click(con_button_x, con_button_y)
    time.sleep(7)
    detect_change(lvl_place_x, lvl_place_y, lvl_place_rgb)
    wait(5)
    wait(11)
    pyautogui.press('Enter')
    time.sleep(0.5)
    pyautogui.press('/')
    time.sleep(0.5)
    pyautogui.press('f', presses=2)
    time.sleep(0.5)
    pyautogui.press('Enter')
    time.sleep(3)
    pyautogui.click(surr_button_x, surr_button_y)
    wait(1)
    pyautogui.click(con_button_x, con_button_y)
    time.sleep(1)
    print("Ziv is gay")


def main():
    print("We are not responsible for any actions legal or not that rito will take against joe @$$")
    while 'Ziv is at the army':
        play_game()
