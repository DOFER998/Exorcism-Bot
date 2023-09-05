from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Seasons(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    type: Optional[str] | None
    startTime: Optional[datetime] | None
    endTime: Optional[datetime] | None
    parentUuid: Optional[str] | None
    assetPath: Optional[str] | None
