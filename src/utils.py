from config import PATH_TO_RESOURCES

def load_messages_for_bot(name: str) -> str:
    with open(PATH_TO_RESOURCES / "messages" / f"{name}.txt", encoding="utf-8") as file:
        return file.read()

def load_prompt(name: str) -> str:
    with open(PATH_TO_RESOURCES / "prompts" / f"{name}.txt", encoding="utf-8") as file:
        return file.read()

def get_image_path(name: str) -> str:
    return str(PATH_TO_RESOURCES / "images" / f"{name}.jpg")