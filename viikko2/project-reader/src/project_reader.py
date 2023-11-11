from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        conv_string = toml.loads(content)
        poetry_config = conv_string["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(poetry_config["name"], poetry_config["description"],poetry_config["dependencies"], poetry_config["group"]["dev"]["dependencies"], poetry_config["license"],poetry_config["authors"])
