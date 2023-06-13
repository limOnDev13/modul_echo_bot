from environs import Env
from dataclasses import dataclass


@dataclass
class Tg_bot:
    token: str


@dataclass
class Config:
    tg_bot: Tg_bot


def export_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)
    config: Config = Config(tg_bot=Tg_bot(token=env('TOKEN')))
    return config
