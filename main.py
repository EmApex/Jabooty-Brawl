#Fixed by Jordan. You're welcome.
from config import *
import time
import logging
import asyncio
import sys
import os

from buttplug import *

import log_tailer
import vibration_handler

if not os.path.isfile("config.py"):
    print("Copy config_default.py to config.py and edit it to set up!")
    exit()

async def main(logfile):
    client = Client("Jabuttri Brawl")  # :3

    connector = WebsocketConnector(INTIFACE_SERVER_ADDR, logger=client.logger)

    console = log_tailer.LogTail(logfile)
    _ = console.read()

    try:
        await client.connect(connector)
    except:
        logging.error("Could not connect!")
        return

    client.logger.info("Connected to Intiface!")

    if len(client.devices) == 0:
        logging.error("No devices!")
        return

    # get steam username to detect killfeed data
    name = None
    logging.info("Getting name...")
    while name is None:
        try:
            name = STEAM_NAME
        except Exception as e:
            print(e)
            sys.exit()

    logging.info(f"Got name: {name}")
    logging.info("Ready to play!")

    vibe = vibration_handler.VibrationHandler(logging)
    
    killstreak = 0
    killtime = 0

    while True:
        # detect kills & class / weapon switches from console log
        while True:
            line = console.read_line()
            
            if line is None:
                break
            
            lineList = line.split("killed")
            if len(lineList) == 1:
                break
            
            killer = lineList[0][:-1]
            deader = lineList[1].split(" with")[0][1:]
            #print(killer)
            #print(deader)
            
            if killer == name:  # we got a kill
                #print(time.time() - killtime)
                if time.time() - killtime  > 5:
                    killstreak = 0
                    vibe.kill(kstreak = killstreak)
                    print("Streak reset")
                else:
                    killstreak += 1
                    vibe.kill(kstreak = killstreak)
                    print("Streak: " + str(killstreak))
                killtime = time.time()
                #print(killtime)
            if deader == name:  # we died :)
                print("Death")
                vibe.death()
            print(line)
            

        # run vibrator
        await vibe.run_buzz(devices=client.devices)
        await asyncio.sleep(1.0 / UPDATE_SPEED)

if __name__ == "__main__":
    print("Ensure Intiface Central is running and has your device connected")
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    with open(CONSOLE_LOG, "r", encoding = "utf-8") as f:
        asyncio.run(main(f))
