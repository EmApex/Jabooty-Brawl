# Jabuttri Brawl

Controls smart sex toys based on kills and deaths in Jabroni Brawl, using the Intiface Central backbone to connect to hardware

WARNING - Use only in private lobbies / servers with consenting players, and test your strengths before using them. The default values are ad-hoc and not suitable for every person or device

# Features
- Custom vibration strength and time for kills and deaths
- Multipliers for killstreaks

# Setup
Add "-condebug -conclearlog" to your launch options.

Copy config_default.py to config.py (you will have to create this file in the same directory as config_default.py) and fill out your Steam username (or another player's name!) and console.log path (console.log will be in the base Jabroni Brawl install folder)

# Customising for multiple devices/motors

Edit the run_buzz method in vibration_handler.py to your liking
