from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Themes(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    displayIcon: Optional[str] | None
    storeFeaturedImage: Optional[str] | None
    assetPath: Optional[str] | None
