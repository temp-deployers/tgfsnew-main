from os import environ
from typing import Dict, Optional

class TokenParser:
    def __init__(self, config_file: Optional[str] = None):
        self.tokens = {}
        self.config_file = config_file

    def parse_from_env(self) -> Dict[int, str]:
        self.tokens = dict(
            (c + 1, t)
            for c, (_, t) in enumerate(
                filter(
                    lambda n: n[0].startswith("MULTI_TOKEN"), sorted(environ.items())
                )
            )
        )
        return self.tokens

    def get_github_token(self) -> str:
        return environ.get("GITHUB_TOKEN")

    def get_github_username(self) -> str:
        return environ.get("GITHUB_USERNAME")

    def get_github_repo(self) -> str:
        return environ.get("GITHUB_REPO")
