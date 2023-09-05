from typing import Optional, List

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class GameFeatureOverrides(BaseModel):
    featureName: Optional[str] | None
    state: Optional[bool] | None


class GameRuleBoolOverrides(BaseModel):
    ruleName: Optional[str] | None
    state: Optional[bool] | None


class Gamemodes(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    duration: Optional[Language] | None
    economyType: Optional[str] | None
    allowsMatchTimeouts: Optional[bool] | None
    isTeamVoiceAllowed: Optional[bool] | None
    isMinimapHidden: Optional[bool] | None
    orbCount: Optional[int] | None
    roundsPerHalf: Optional[int] | None
    teamRoles: Optional[List[str]] | None
    gameFeatureOverrides: Optional[List[GameFeatureOverrides]] | None
    gameRuleBoolOverrides: Optional[List[GameRuleBoolOverrides]] | None
    displayIcon: Optional[str] | None
    assetPath: Optional[str] | None
