from typing import Optional, List

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language, Location


class Callouts(BaseModel):
    regionName: Optional[Language] | None
    superRegionName: Optional[Language] | None
    location: Optional[Location] | None


class Maps(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    narrativeDescription: Optional[Language] | None
    tacticalDescription: Optional[Language] | None
    coordinates: Optional[Language] | None
    displayIcon: Optional[str] | None
    listViewIcon: Optional[str] | None
    splash: Optional[str] | None
    assetPath: Optional[str] | None
    mapUrl: Optional[str] | None
    xMultiplier: Optional[float] | None
    yMultiplier: Optional[float] | None
    xScalarToAdd: Optional[float] | None
    yScalarToAdd: Optional[float] | None
    callouts: Optional[List[Callouts]] | None
