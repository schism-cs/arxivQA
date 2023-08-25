import toml


def load_config():
    data = toml.load("config.toml")
    return data
