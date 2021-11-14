from pynput.keyboard import Key, Controller
from time import sleep


def main():
    print("This is the most useless python application you'll see")
    sleep(2)
    key_controller = Controller()
    print("Check out what it's about to do")
    sleep(2)
    key_controller.press(Key.alt)
    key_controller.press(Key.f4)
    key_controller.release(Key.alt)
    key_controller.release(Key.f4)
    key_controller.press(Key.enter)
    key_controller.release(Key.enter)


if __name__ == '__main__':
    main()
