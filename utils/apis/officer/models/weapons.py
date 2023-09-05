from typing import Optional, List

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language, GridPosition


class AdsStats(BaseModel):
    zoomMultiplier: Optional[float] | None
    fireRate: Optional[float] | None
    runSpeedMultiplier: Optional[float] | None
    burstCount: Optional[int] | None
    firstBulletAccuracy: Optional[float] | None


class AltShotgunStats(BaseModel):
    shotgunPelletCount: Optional[int] | None
    burstRate: Optional[float] | None


class AirBurstStats(BaseModel):
    shotgunPelletCount: Optional[int] | None
    burstDistance: Optional[float] | None


class DamageRanges(BaseModel):
    rangeStartMeters: Optional[float] | None
    rangeEndMeters: Optional[float] | None
    headDamage: Optional[float] | None
    bodyDamage: Optional[float] | None
    legDamage: Optional[float] | None


class WeaponStats(BaseModel):
    fireRate: Optional[float] | None
    magazineSize: Optional[int] | None
    runSpeedMultiplier: Optional[float] | None
    equipTimeSeconds: Optional[float] | None
    reloadTimeSeconds: Optional[float] | None
    firstBulletAccuracy: Optional[float] | None
    shotgunPelletCount: Optional[int] | None
    wallPenetration: Optional[str] | None
    feature: Optional[str] | None
    fireMode: Optional[str] | None
    altFireType: Optional[str] | None
    adsStats: Optional[AdsStats] | None
    altShotgunStats: Optional[AltShotgunStats] | None
    airBurstStats: Optional[AirBurstStats] | None
    damageRanges: Optional[List[DamageRanges]] | None


class ShopData(BaseModel):
    cost: Optional[int] | None
    category: Optional[str] | None
    categoryText: Optional[Language] | None
    gridPosition: Optional[GridPosition] | None
    canBeTrashed: Optional[bool] | None
    image: Optional[str] | None
    newImage: Optional[str] | None
    newImage2: Optional[str] | None
    assetPath: Optional[str] | None


class Chromas(BaseModel):
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    displayIcon: Optional[str] | None
    fullRender: Optional[str] | None
    swatch: Optional[str] | None
    streamedVideo: Optional[str] | None
    assetPath: Optional[str] | None


class Levels(BaseModel):
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    levelItem: Optional[str] | None
    displayIcon: Optional[str] | None
    streamedVideo: Optional[str] | None
    assetPath: Optional[str] | None


class Skins(BaseModel):
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    themeUuid: Optional[str] | None
    contentTierUuid: Optional[str] | None
    displayIcon: Optional[str] | None
    wallpaper: Optional[str] | None
    assetPath: Optional[str] | None
    chromas: Optional[List[Chromas]] | None
    levels: Optional[List[Levels]] | None


class Weapons(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    category: Optional[str] | None
    defaultSkinUuid: Optional[str] | None
    displayIcon: Optional[str] | None
    killStreamIcon: Optional[str] | None
    assetPath: Optional[str] | None
    weaponStats: Optional[WeaponStats] | None
    shopData: Optional[ShopData] | None
    skins: Optional[List[Skins]] | None
