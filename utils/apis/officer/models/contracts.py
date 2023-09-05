from typing import Optional, List

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Reward(BaseModel):
    type: Optional[str] | None
    uuid: Optional[str] | None
    amount: Optional[int] | None
    isHighlighted: Optional[bool] | None


class Levels(BaseModel):
    reward: Optional[Reward] | None
    xp: Optional[int] | None
    vpCost: Optional[int] | None
    isPurchasableWithVP: Optional[bool] | None
    doughCost: Optional[int] | None
    isPurchasableWithDough: Optional[bool] | None


class FreeRewards(BaseModel):
    type: Optional[str] | None
    uuid: Optional[str] | None
    amount: Optional[int] | None
    isHighlighted: Optional[bool] | None


class Chapters(BaseModel):
    isEpilogue: Optional[bool] | None
    levels: Optional[List[Levels]] | None
    freeRewards: Optional[List[FreeRewards]] | None


class Content(BaseModel):
    relationType: Optional[str] | None
    relationUuid: Optional[str] | None
    chapters: Optional[List[Chapters]] | None
    premiumRewardScheduleUuid: Optional[str] | None
    premiumVPCost: Optional[int] | None


class Contracts(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    displayIcon: Optional[str] | None
    shipIt: Optional[bool] | None
    freeRewardScheduleUuid: Optional[str] | None
    content: Optional[Content] | None
    assetPath: Optional[str] | None
