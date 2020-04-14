from threading import Thread
import time
from lights import rainbow, rainbow_cycle, color_fill, num_pixels, theather_chase, rainbow_theather_chase


class light_thread(Thread):
    def __init__(self, thread_id):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.should_exit = False
        self.color = (255, 255, 255)
        self.active_pixels = 0
        self.speed = 20

    def run(self):
        print("Starting: ")
        rainbow_cycle_iteration = 0
        while self.should_exit is False:
            self.increment_active_pixel()
            if(self.method is 'rainbow'):
                rainbow(self.active_pixels)

            elif(self.method is 'fill'):
                color_fill(self.color, self.active_pixels)
            elif self.method is 'rainbow_cycle':
                rainbow_cycle(self.active_pixels, rainbow_cycle_iteration)
                rainbow_cycle_iteration += 1
            elif self.method is 'rainbow_theather_chase':
                rainbow_theather_chase(
                    rainbow_cycle_iteration, self.active_pixels)
            elif self.method is 'theather_chase':
                theather_chase(
                    self.color, rainbow_cycle_iteration, self.active_pixels)
                rainbow_cycle_iteration += 1
            else:
                color_fill(self.color, self.active_pixels)
            time.sleep(self.speed/1000)

        print("Exiting: ")

    def increment_active_pixel(self):
        if(self.active_pixels < num_pixels):
            self.active_pixels += 1

    def reset_active_pixel(self):
        self.active_pixels = 0

    def set_method(self, method):
        self.method = methods[method]

    def set_color(self, color):
        self.color = color

    def get_parameters(self):
        color = self.color
        return {
            'method': self.method,
            'red': color[0],
            'green': color[1],
            'blue': color[2]
        }

    def set_speed(self, speed):
        self.speed = speed


methods = {
    'rainbow': 'rainbow',
    'rainbow_cycle': 'rainbow_cycle',
    'theather_chase': 'theather_chase',
    'rainbow_theather_chase': 'rainbow_theather_chase',
    'color_fill': 'color_fill'
}
