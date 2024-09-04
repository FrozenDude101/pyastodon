from dataclasses import dataclass

from pyastodon.models.base.objectModel import ObjectModel


@dataclass()
class InstanceConfigurationMediaAttachmentsModel(ObjectModel):
    supported_mime_types: list[str]
    image_size_limit: int
    image_matrix_limit: int
    video_size_limit: int
    video_frame_rate_limit: int
    video_matrix_limit: int