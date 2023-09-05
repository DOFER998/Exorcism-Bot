from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class PlayerTitles(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    titleText: Optional[Language] | None
    isHiddenIfNotOwned: Optional[bool] | None
    assetPath: Optional[str] | None
