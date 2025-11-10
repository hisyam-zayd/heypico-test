"""
title: HeyPico AI - Nearby Restaurants
author: Hisyam Zayd
git_url: https://github.com/hisyam-zayd/heypico-test
description: Tools for get nearby restaurant and show embedded maps for directions
required_open_webui_version: 0.6.0
requirements: 
version: 0.1.0
license: MIT
"""

from typing import Literal, List
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse

class Tools:
    class Valves(BaseModel):
        API_KEY_MAPS_EMBED: str = Field(
            default=None,
            description="API key for embedded Google Maps",
            required=True
        )
        API_KEY_GEOCODING: str = Field(
            default=None,
            description="API key for Google Maps - Geocoding",
            required=True
        )
        pass

    def __init__(self):
        self.valves = self.Valves()
        pass

    def _do_geocode_into_name(
        self,
        latitude: float,
        longitude: float
    ) -> str:
        pass

    def _validate_oauth(
        self,
        oauth_token: dict
    ) -> bool:
        pass

    async def get_nearby_restaurant(
        self,
        text_query: str,
        latitude: float,
        longitude: float,
        rank_preference: Literal[
            "DISTANCE",
            "RELEVANCE"
        ] = "DISTANCE",
        included_type: Literal[
            "restaurant",
            "american_restaurant",
            "asian_restaurant",
            "bakery",
            "bar",
            "breakfast_restaurant",
            "brunch_restaurant",
            "cafe",
            "cafeteria",
            "chinese_restaurant",
            "coffee_shop",
            "dessert_restaurant",
            "donut_shop",
            "fast_food_restaurant",
            "food_court",
            "french_restaurant",
            "hamburger_restaurant",
            "ice_cream_shop",
            "indian_restaurant",
            "indonesian_restaurant",
            "italian_restaurant",
            "japanese_restaurant",
            "juice_shop",
            "korean_restaurant",
            "middle_eastern_restaurant",
            "pizza_restaurant",
            "ramen_restaurant",
            "seafood_restaurant",
            "spanish_restaurant",
            "steak_house",
            "sushi_restaurant",
            "thai_restaurant",
            "vietnamese_restaurant"
        ] = "restaurant",
        open_now: bool = True,
        min_rating: float = 4.0,
        page_size: int = 5,
        price_level: Literal[
            "PRICE_LEVEL_UNSPECIFIED",
            "PRICE_LEVEL_FREE",
            "PRICE_LEVEL_INEXPENSIVE",
            "PRICE_LEVEL_MODERATE",
            "PRICE_LEVEL_EXPENSIVE",
            "PRICE_LEVEL_VERY_EXPENSIVE"
        ] = "PRICE_LEVEL_UNSPECIFIED",
        travel_mode: Literal[
            "DRIVE",
            "BICYCLE",
            "WALK",
            "TWO_WHEELER"
        ] = "DRIVE",
        routing_preference: Literal[
            "TRAFFIC_UNAWARE",
            "TRAFFIC_AWARE",
            "TRAFFIC_AWARE_OPTIMAL"
        ] = "TRAFFIC_UNAWARE",
        __event_emitter__ = None,
        __user__: dict = None,
        __metadata__: dict = None,
        __oauth_token__: dict = None
    ) -> List[str]:
        pass

    async def show_directions_embed(
        self,
        origin_latitude: float,
        origin_longiude: float,
        destination_name: str,
        travel_mode: Literal[
            "DRIVE",
            "BICYCLE",
            "WALK",
            "TWO_WHEELER"
        ] = "DRIVE",
        __event_emitter__ = None,
        __user__: dict = None,
        __metadata__: dict = None,
        __oauth_token__: dict = None
    ) -> HTMLResponse:
        pass