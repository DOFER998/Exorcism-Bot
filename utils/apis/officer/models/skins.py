from typing import Optional, List

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Chromas(BaseModel):
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    displayIcon: Optional[str] | None
    fullRender: Optional[str] | None
    swatch: Optional[str] | None
    streamedVideo: Optional[str] | None
    assetPath: Optional[str] | None


class Levels(BaseModel):
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    levelItem: Optional[str] | None
    displayIcon: Optional[str] | None
    streamedVideo: Optional[str] | None
    assetPath: Optional[str] | None


class Skins(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    themeUuid: Optional[str] | None
    contentTierUuid: Optional[str] | None
    displayIcon: Optional[str] | None
    wallpaper: Optional[str] | None
    assetPath: Optional[str] | None
    chromas: Optional[List[Chromas]] | None
    levels: Optional[List[Levels]] | None
