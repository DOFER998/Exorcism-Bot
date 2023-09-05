from typing import Optional, List

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Tiers(BaseModel):
    tier: Optional[int] | None
    tierName: Optional[Language] | None
    division: Optional[str] | None
    divisionName: Optional[Language] | None
    color: Optional[str] | None
    backgroundColor: Optional[str] | None
    smallIcon: Optional[str] | None
    largeIcon: Optional[str] | None
    rankTriangleDownIcon: Optional[str] | None
    rankTriangleUpIcon: Optional[str] | None


class CompetitiveTiers(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    assetObjectName: Optional[str] | None
    tiers: Optional[List[Tiers]] | None
    assetPath: Optional[str] | None
