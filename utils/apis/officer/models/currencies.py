from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Currencies(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    displayNameSingular: Optional[Language] | None
    displayIcon: Optional[str] | None
    largeIcon: Optional[str] | None
    assetPath: Optional[str] | None
