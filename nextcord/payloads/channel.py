# The MIT License (MIT)
# Copyright (c) 2021-present vcokltfre & tag-epic
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from datetime import datetime
    from typing import Annotated, NotRequired, Optional, ValueRange

    from ..enums import ChannelType, VideoQualityMode
    from ..types.permissions import PermissionOverwrite
    from ..types.snowflake import Snowflake


class ChannelPayload(TypedDict):
    id: Snowflake
    type: ChannelType
    guild_id: NotRequired[Snowflake]
    position: NotRequired[int]
    permission_overwrites: NotRequired[list[PermissionOverwrite]]
    name: NotRequired[str]
    nsfw: NotRequired[bool]
    parent_id: NotRequired[Optional[Snowflake]]


class CategoryChannelPayload(ChannelPayload):
    ...


class MessageablePayload(ChannelPayload):
    last_message_id: Optional[int]
    last_pin_timestamp: NotRequired[Optional[datetime]]
    default_auto_archive_duration: NotRequired[int]
    permissions: NotRequired[str]


# class DMChannelPayload(ChannelPayload):
#     recipients: NotRequired[list[User]]
#     icon: NotRequired[Optional[str]]
#     owner_id: NotRequired[Snowflake]
#     application_id: NotRequired[Snowflake]


class TextChannelPayload(ChannelPayload, MessageablePayload):
    topic: Optional[str]
    rate_limit_per_user: Annotated[int, ValueRange(0, 21600)]


class NewsChannelPayload(ChannelPayload, MessageablePayload):
    topic: Optional[str]


class ThreadChannelPayload(ChannelPayload, MessageablePayload):
    rate_limit_per_user: Annotated[int, ValueRange(0, 21600)]
    message_count: int
    member_count: int
    thread_metadata: ThreadMetadata
    member: NotRequired[ThreadMember]


class VoiceChannelPayload(ChannelPayload):
    bitrate: int
    user_limit: int
    rtc_region: Optional[str]
    video_quality_mode: NotRequired[VideoQualityMode]


class ThreadMetadata(TypedDict):
    archived: bool
    auto_archive_duration: int
    archive_timestamp: datetime
    locked: bool
    invitable: NotRequired[bool]


class ThreadMember(TypedDict):
    id: NotRequired[Snowflake]
    user_id: NotRequired[Snowflake]
    join_timestamp: datetime
    flags: int
