# The MIT License (MIT)
#
# Copyright (c) 2021-present vcokltfre & tag-epic
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
from __future__ import annotations

from asyncio.futures import Future
from typing import TYPE_CHECKING

from .protocols.gateway import GatewayProtocol

if TYPE_CHECKING:
    from typing import Any, Optional

    from .protocols.http import HTTPClient
    from .type_sheet import TypeSheet


class Gateway(GatewayProtocol):
    def __init__(
        self,
        type_sheet: TypeSheet,
        http: HTTPClient,
        *,
        status: Any = None,
        presence: Any = None,
        shard_count: Optional[int] = None
    ):
        self.type_sheet: TypeSheet = type_sheet
        self.http: HTTPClient = http
        self._error_future: Future = Future()

        # Shard count
        self.shard_count: Optional[int] = shard_count
        self.current_shard_count: Optional[int] = shard_count

        # Shard sets
        self.shards: list[Any] = []
        # When we get disconnected for too low shard count, we start creating a second set of inactive shards.
        self._pending_shard_set: list[Any] = []
        self.recreating_shards: bool = False

    async def connect(self):
        # TODO: Connect

        await self._error_future
