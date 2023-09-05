from typing import Optional

from pydantic import BaseModel, Field


class LevelBorders(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    startingLevel: Optional[int] | None
    levelNumberAppearance: Optional[str] | None
    smallPlayerCardAppearance: Optional[str] | None
    assetPath: Optional[str] | None
