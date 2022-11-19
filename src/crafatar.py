from os import getcwd
from pathlib import Path
from requests import get
from random import randint

class Crafatar:
	def __init__(self, player_uuid: str) -> None:
		self.api = "https://crafatar.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
		self.player_uuid = player_uuid

	def save_file(
			self,
			content: bytes,
			location: str = getcwd()) -> bool:
		with open(
			Path(location).joinpath(f"{randint(0, 86400)}-{self.player_uuid}.png"),
			mode="wb+",
		) as file:
			file.write(content)
			file.close()
		return True

	def get_player_avatar(self, size: int = 100) -> bool:
		response = get(
			f"{self.api}/avatars/{self.player_uuid}", 
			headers=self.headers).content
		return self.save_file(content=response)

	def get_player_head(self) -> bool:
		response = get(
			f"{self.api}/renders/head/{self.player_uuid}",
			headers=self.headers).content
		return self.save_file(content=response)

	def get_player_body(self) -> bool:
		response = get(
			f"{self.api}/renders/body/{self.player_uuid}",
			headers=self.headers).content
		return self.save_file(content=response)

	def get_player_skin(self) -> bool:
		response = get(
			f"{self.api}/skins/{self.player_uuid}",
			headers=self.headers).content
		return self.save_file(content=response)

	def get_player_cape(self) -> bool:
		response = get(
			f"{self.api}/capes/{self.player_uuid}",
			headers=self.headers).content
		return self.save_file(content=response)
