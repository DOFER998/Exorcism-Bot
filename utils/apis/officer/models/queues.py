from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Queues(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    queueId: Optional[str] | None
    displayName: Optional[Language] | None
    description: Optional[Language] | None
    dropdownText: Optional[Language] | None
    selectedText: Optional[Language] | None
    isBeta: Optional[bool] | None
    displayIcon: Optional[str] | None
    assetPath: Optional[str] | None
