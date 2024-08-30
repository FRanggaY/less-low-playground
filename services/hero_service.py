from repositories.hero_repository import HeroRepository

class HeroService:
    def __init__(self, name: str):
        self.name = name
        self.hero_repository = HeroRepository(name)