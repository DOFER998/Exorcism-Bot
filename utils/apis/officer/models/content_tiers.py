from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class ContentTiers(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    devName: Optional[str] | None
    rank: Optional[int] | None
    juiceValue: Optional[int] | None
    juiceCost: Optional[int] | None
    highlightColor: Optional[str] | None
    displayIcon: Optional[str] | None
    assetPath: Optional[str] | None
