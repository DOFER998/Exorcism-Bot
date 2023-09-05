from typing import Optional, List

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Levels(BaseModel):
    uuid: Optional[str] | None
    sprayLevel: Optional[int] | None
    displayName: Optional[Language] | None
    displayIcon: Optional[str] | None
    assetPath: Optional[str] | None


class Sprays(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    category: Optional[str] | None
    themeUuid: Optional[str] | None
    isNullSpray: Optional[bool] | None
    hideIfNotOwned: Optional[bool] | None
    displayIcon: Optional[str] | None
    fullIcon: Optional[str] | None
    fullTransparentIcon: Optional[str] | None
    animationPng: Optional[str] | None
    animationGif: Optional[str] | None
    assetPath: Optional[str] | None
    levels: Optional[List[Levels]] | None
