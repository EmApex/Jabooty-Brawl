CONSOLE_LOG = "G:\\SteamLibrary\\steamapps\\common\\Jabroni Brawl Episode 3\\console.log"
# Replace this with your own log path!

STEAM_NAME = "YOUR NAME HERE" # Paste your Steam name (or somebody else's) here

INTIFACE_SERVER_ADDR = "ws://127.0.0.1:12345"  # The address intiface central is listening on

UPDATE_SPEED = 5  # Speed in updates per second, values higher than 10 are not recommended for performance

BASE_VIBE = 0.0  # Base vibration speed that motor will always be on

KILL_STRENGTH = 0.2  # Base kill vibration strength (0 to disable)
KILL_TIME = 1  # Kill vibration time

# When at KILLSTREAK_MAX, vibration strength is KILL_STRENGTH * KILLSTREAK_STRENGTH_MULTIPLIER
# When you get first kill, vibration strength is KILL_STRENGTH * 1.0
KILLSTREAK_STRENGTH_MULTIPLIER = 5  # Amount that reaching KILLSTREAK_MAX should multiply strength
KILLSTREAK_TIME_MULTIPLIER = 1.5  # Amount that reaching KILLSTREAK_MAX should multiply time

KILLSTREAK_MAX = 6  # Max killstreak for scaling

DEATH_STRENGTH = 0.1  # Death vibration strength
DEATH_TIME = 0  # Death vibration time
