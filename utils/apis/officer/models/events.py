from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Events(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    shortDisplayName: Optional[Language] | None
    startTime: Optional[datetime] | None
    endTime: Optional[datetime] | None
    assetPath: Optional[str] | None
