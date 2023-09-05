from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class PlayerCards(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    isHiddenIfNotOwned: Optional[bool] | None
    themeUuid: Optional[str] | None
    displayIcon: Optional[str] | None
    smallArt: Optional[str] | None
    wideArt: Optional[str] | None
    largeArt: Optional[str] | None
    assetPath: Optional[str] | None
