import time
from config import *

class VibrationHandler:
    def __init__(self, logger):
        self.logger = logger
        self.timed_buzzes = []  # list of timed vibration activations
        self._curr_strength = 0  # current strength priv variable
        self.last_strength = 0

    @property
    def current_strength(self):
        return self._curr_strength

    @current_strength.setter
    def current_strength(self, new_strength):
        if new_strength > self._curr_strength:
            self._curr_strength = new_strength

    def timed_buzz(self, strength, time_end):
        self.timed_buzzes.append((strength, time.time() + time_end))

    def death(self):
        self.timed_buzz(DEATH_STRENGTH, DEATH_TIME)

    def kill(self, kstreak, crit=False):
        killstreak_coeff = min(kstreak, KILLSTREAK_MAX) / KILLSTREAK_MAX

        strength = KILL_STRENGTH * \
                   (killstreak_coeff * (KILLSTREAK_STRENGTH_MULTIPLIER - 1.0) + 1.0)
        time = KILL_TIME * \
               (killstreak_coeff * (KILLSTREAK_TIME_MULTIPLIER - 1.0) + 1.0)

        self.timed_buzz(strength, time)

    def update(self):
        self.last_strength = self.current_strength
        self._curr_strength = BASE_VIBE

        now = time.time()

        for timer in self.timed_buzzes:
            if now <= timer[1]:
                self.current_strength = timer[0]

        self.timed_buzzes = list(filter(lambda x: x[1] > now, self.timed_buzzes))

        return self.current_strength

    # Takes a list of devices and activates devices based on vibration handling
    async def run_buzz(self, devices):
        vibe_strength = self.update()

        # activate all actuators
        for device in devices.values():
            for actuator in device.actuators:
                await actuator.command(vibe_strength)
        #
        # could also do this
        # await devices[0].actuators[0].command(vibe_strength)
        # await devices[0].actuators[1].command(vibe_strength * 0.5)
        # etc.
