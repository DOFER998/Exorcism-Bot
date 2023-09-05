from typing import Optional

from pydantic import BaseModel, Field

from utils.apis.officer.models.general import Language


class Bundles(BaseModel):
    id: Optional[str] | None = Field(alias='_id')
    uuid: Optional[str] | None
    displayName: Optional[Language] | None
    displayNameSubText: Optional[Language] | None
    description: Optional[Language] | None
    extraDescription: Optional[Language] | None
    promoDescription: Optional[Language] | None
    useAdditionalContext: Optional[bool] | None
    displayIcon: Optional[str] | None
    displayIcon2: Optional[str] | None
    verticalPromoImage: Optional[str] | None
    assetPath: Optional[str] | None
