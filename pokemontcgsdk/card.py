from dataclasses import dataclass
from typing import Optional, List

from pokemontcgsdk.ability import Ability
from pokemontcgsdk.ancienttrait import AncientTrait
from pokemontcgsdk.attack import Attack
from pokemontcgsdk.cardimage import CardImage
from pokemontcgsdk.legality import Legality
from pokemontcgsdk.querybuilder import QueryBuilder
from pokemontcgsdk.resistance import Resistance
from pokemontcgsdk.set import Set
from pokemontcgsdk.tcgplayer import TCGPlayer
from pokemontcgsdk.weakness import Weakness

@dataclass
class Card():
    RESOURCE = 'cards'

    abilities: Optional[List[Ability]]
    artist: Optional[str]
    ancientTrait: Optional[AncientTrait]
    attacks: Optional[List[Attack]]
    convertedRetreatCost: Optional[int]
    evolvesFrom: Optional[str]
    flavorText: Optional[str]
    hp: Optional[str]
    id: str
    images: CardImage
    legalities: Legality
    name: str
    nationalPokedexNumbers: Optional[List[int]]
    number: Optional[str]
    rarity: Optional[str]
    resistances: Optional[List[Resistance]]
    retreatCost: Optional[List[str]]
    rules: Optional[List[str]]
    set: Set
    subtypes: Optional[List[str]]
    supertype: Optional[str]
    tcgplayer: Optional[TCGPlayer]
    types: Optional[List[str]]
    weaknesses: Optional[List[Weakness]]

    @staticmethod
    def find(id):
        return QueryBuilder(Card, Card.transform).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Card, Card.transform).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Card, Card.transform).all()

    @staticmethod
    def transform(response):
        if response.get('tcgplayer', {}).get('prices', {}).get('1stEditionNormal'):
            response['tcgplayer']['prices']['firstEditionNormal'] = response['tcgplayer']['prices'].pop('1stEditionNormal')
        if response.get('tcgplayer', {}).get('prices', {}).get('1stEditionHolofoil'):
            response['tcgplayer']['prices']['firstEditionHolofoil'] = response['tcgplayer']['prices'].pop('1stEditionHolofoil')
        return response
