import webbrowser
from openai import OpenAI
import user_config

client = OpenAI(api_key=user_config.openai_key)

def generate_image(prompt):
    if not prompt or prompt.strip() == "":
        print("Prompt is empty. Cannot generate image.")
        return

    try:
        response = client.images.generate(
            model="dall-e-3",  # or "dall-e-2" if needed
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        print("Generated image URL:", image_url)
        webbrowser.open(image_url)

    except Exception as e:
        print("OpenAI Error:", e)