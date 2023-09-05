from typing import Optional, List

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Levels(BaseModel):
    uuid: Optional[str] | None
    charmLevel: Optional[int] | None
    hideIfNotOwned: Optional[bool] | None
    displayName: Optional[Language] | None
    displayIcon: Optional[str] | None
    assetPath: Optional[str] | None


class Buddies(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    isHiddenIfNotOwned: Optional[bool] | None
    themeUuid: Optional[str] | None
    displayIcon: Optional[str] | None
    assetPath: Optional[str] | None
    levels: Optional[List[Levels]] | None
