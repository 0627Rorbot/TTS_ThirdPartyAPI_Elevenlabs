# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel


class NormalizedAlignment(UncheckedBaseModel):
    """
    Alignment information for the generated audio given the input normalized text sequence.
    """

    char_start_times_ms: typing.Optional[typing.List[int]] = pydantic_v1.Field(default=None)
    """
    A list of starting times (in milliseconds) for each character in the normalized text as it
    corresponds to the audio. For instance, the character 'H' starts at time 0 ms in the audio.  
    Note these times are relative to the returned chunk from the model, and not the
    full audio response.
    """

    chars_durations_ms: typing.Optional[typing.List[int]] = pydantic_v1.Field(default=None)
    """
    A list of durations (in milliseconds) for each character in the normalized text as it
    corresponds to the audio. For instance, the character 'H' lasts for 3 ms in the audio.  
    Note these times are relative to the returned chunk from the model, and not the
    full audio response.
    """

    chars: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    A list of characters in the normalized text sequence. For instance, the first character is 'H'.
    Note that this list may contain spaces, punctuation, and other special characters.
    The length of this list should be the same as the lengths of `char_start_times_ms` and `chars_durations_ms`.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
