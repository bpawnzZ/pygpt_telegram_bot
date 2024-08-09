import os
import yaml
from dotenv import load_dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
load_dotenv()

# config parameters
telegram_token = os.getenv('TELEGRAM_TOKEN') or 'wow_so_secret'

openai_api_key = os.getenv('OPEN_AI_KEY') or 'wow_so_secret'

# leave null to use default api base or you can put your own base url here
_api_base = os.getenv('OPEN_AI_API_BASE') or ''
openai_api_base = None if _api_base == '' else _api_base 

# new dialog starts after timeout (in seconds)
new_dialog_timeout = os.getenv('DIALOG_TIMEOUT') or 600

# if set, messages will be shown to user word-by-word
enable_message_streaming = True if os.getenv('ENABLE_MESSAGE_STREAMING') == 'True' else False

return_n_generated_images = os.getenv('GENERATE_IMAGES_COUNT') or 1
# the image size for image generation. Generated images can have a size of 256x256, 512x512, or 1024x1024 pixels. Smaller sizes are faster to generate.
image_size = os.getenv('IMAGE_SIZE') or '512x512'

n_chat_modes_per_page = os.getenv('CHAT_MODE_PER_PAGE') or 5

mongodb_port = os.getenv('MONGODB_PORT') or '27017'
mongodb_uri = f"mongodb://mongo:{mongodb_port}"

allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
# TODO: help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
