import cv2
import time

from waiting import wait

from output_fxns import get_window_info, get_full_screen, onHomeMenu, onKeepHand, locate_leftmost_playable_card
from input_fxns import click_on, print_coord, playCardAt

if __name__ == "__main__":

    window_info = get_window_info()

    # make sure MTGA resolution is 1920x1080 and full screen
    window_info['width_fullscreen'] = 1920
    window_info['height_fullscreen'] = 1080

    wait(lambda: onHomeMenu(window_info), timeout_seconds=120, waiting_for='MTGA_BOT: waiting for home menu')
    while(onHomeMenu(window_info)):
        click_on('PLAY_GAME')

    wait(lambda: onKeepHand(window_info), timeout_seconds=120, waiting_for='MTGA_BOT: waiting for keep hand')
    click_on('KEEP_HAND')

    while (True):
        time.sleep(1)
        isPlayableCard, leftmost_card_pt = locate_leftmost_playable_card(window_info)
        img = get_full_screen(window_info)
        
        if isPlayableCard:
            playCardAt(window_info, leftmost_card_pt) 
        else:
            click_on('PASS')

