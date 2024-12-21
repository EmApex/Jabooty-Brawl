# Jabooty Brawl

Controls smart sex toys based on kills and deaths in Jabroni Brawl, using the Intiface Central backbone to connect to hardware

Probably doesn't work properly with Linux since the original project has issues

WARNING - Use only in private lobbies / servers with consenting players, and test your strengths before using them. The default values are ad-hoc and not suitable for every person or device

# Features
- Custom vibration strength and time for kills and deaths
- Multipliers for killstreaks

# Setup
Add "-condebug -conclearlog" to your launch options. Then launch the game once to create the console log

Copy config_default.py to config.py (you will have to create this file in the same directory as config_default.py) and fill out your Steam name (or another player's name!) and console.log path (console.log will be in the base Jabroni Brawl install folder)

Only run after launching Jabroni Brawl, as large pre-existing logs can cause the program to get stuck on max intensity. Starting with a clean log avoids these problems

# Customising for multiple devices/motors

Edit the run_buzz method in vibration_handler.py to your liking
