from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Role(BaseModel):
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    description: Optional[Language] | None
    displayIcon: Optional[str] | None
    assetPath: Optional[str] | None


class RecruitmentData(BaseModel):
    counterId: Optional[str] | None
    milestoneId: Optional[str] | None
    milestoneThreshold: Optional[int] | None
    useLevelVpCostOverride: Optional[bool] | None
    levelVpCostOverride: Optional[int] | None
    startDate: Optional[datetime] | None
    endDate: Optional[datetime] | None


class Abilities(BaseModel):
    slot: Optional[str] | None
    displayName: Optional[Language] | None
    description: Optional[Language] | None
    displayIcon: Optional[str] | None


class MediaList(BaseModel):
    id: Optional[int] | None
    wwise: Optional[str] | None
    wave: Optional[str] | None


class VoiceLineItems(BaseModel):
    minDuration: Optional[float] | None
    maxDuration: Optional[float] | None
    mediaList: Optional[List[MediaList]] | None


class VoiceLine(BaseModel):
    en_US: VoiceLineItems | None = Field(alias='en-US')
    de_DE: VoiceLineItems | None = Field(alias='de-DE')
    ar_AE: VoiceLineItems | None = Field(alias='ar-AE')
    es_ES: VoiceLineItems | None = Field(alias='es-ES')
    fr_FR: VoiceLineItems | None = Field(alias='fr-FR')
    es_MX: VoiceLineItems | None = Field(alias='en-US')
    it_IT: VoiceLineItems | None = Field(alias='it-IT')
    ja_JP: VoiceLineItems | None = Field(alias='ja-JP')
    ko_KR: VoiceLineItems | None = Field(alias='ko-KR')
    id_ID: VoiceLineItems | None = Field(alias='id-ID')
    vi_VN: VoiceLineItems | None = Field(alias='vi-VN')
    pl_PL: VoiceLineItems | None = Field(alias='pl-PL')
    pt_BR: VoiceLineItems | None = Field(alias='pt-BR')
    ru_RU: VoiceLineItems | None = Field(alias='ru-RU')
    th_TH: VoiceLineItems | None = Field(alias='th-TH')
    tr_TR: VoiceLineItems | None = Field(alias='tr-TR')
    zh_CN: VoiceLineItems | None = Field(alias='zh-CN')
    zh_TW: VoiceLineItems | None = Field(alias='zh-TW')


class Agents(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    description: Optional[Language] | None
    developerName: Optional[str] | None
    characterTags: Optional[List[Language]] | None
    displayIcon: Optional[str] | None
    displayIconSmall: Optional[str] | None
    bustPortrait: Optional[str] | None
    fullPortrait: Optional[str] | None
    fullPortraitV2: Optional[str] | None
    killfeedPortrait: Optional[str] | None
    background: Optional[str] | None
    backgroundGradientColors: Optional[List[str]] | None
    assetPath: Optional[str] | None
    isFullPortraitRightFacing: Optional[bool] | None
    isPlayableCharacter: Optional[bool] | None
    isAvailableForTest: Optional[bool] | None
    isBaseContent: Optional[bool] | None
    recruitmentData: Optional[RecruitmentData] | None
    role: Optional[Role] | None
    abilities: Optional[List[Abilities]] | None
    voiceLine: Optional[VoiceLine] | None
