from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language, GridPosition


class ShopData(BaseModel):
    cost: Optional[int] | None
    category: Optional[str] | None
    categoryText: Optional[Language] | None
    gridPosition: Optional[GridPosition] | None
    canBeTrashed: Optional[bool] | None
    image: Optional[str] | None
    newImage: Optional[str] | None
    newImage2: Optional[str] | None
    assetPath: Optional[str] | None


class Gear(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    description: Optional[Language] | None
    displayIcon: Optional[str] | None
    assetPath: Optional[str] | None
    shopData: Optional[ShopData] | None
