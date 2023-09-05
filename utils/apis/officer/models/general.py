from typing import Optional

from pydantic import BaseModel, Field


class Language(BaseModel):
    en_US: str | None = Field(alias='en-US')
    de_DE: str | None = Field(alias='de-DE')
    ar_AE: str | None = Field(alias='ar-AE')
    es_ES: str | None = Field(alias='es-ES')
    fr_FR: str | None = Field(alias='fr-FR')
    es_MX: str | None = Field(alias='en-US')
    it_IT: str | None = Field(alias='it-IT')
    ja_JP: str | None = Field(alias='ja-JP')
    ko_KR: str | None = Field(alias='ko-KR')
    id_ID: str | None = Field(alias='id-ID')
    vi_VN: str | None = Field(alias='vi-VN')
    pl_PL: str | None = Field(alias='pl-PL')
    pt_BR: str | None = Field(alias='pt-BR')
    ru_RU: str | None = Field(alias='ru-RU')
    th_TH: str | None = Field(alias='th-TH')
    tr_TR: str | None = Field(alias='tr-TR')
    zh_CN: str | None = Field(alias='zh-CN')
    zh_TW: str | None = Field(alias='zh-TW')


class Location(BaseModel):
    x: Optional[float] | None
    y: Optional[float] | None


class GridPosition(BaseModel):
    row: Optional[int] | None
    column: Optional[int] | None
