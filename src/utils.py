from config import PATH_TO_RESOURCES

def load_messages_for_bot(name: str) -> str:
    with open(PATH_TO_RESOURCES / f"{name}.txt", encoding="utf-8") as file:
        return file.read()