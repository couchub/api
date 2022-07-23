"""
Copyright 2021-2022 Derailed.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from enum import Enum


class Relation(Enum):
    FRIEND = 0
    BLOCKED = 1
    INCOMING = 2
    OUTGOING = 3


class ActivityType(Enum):
    GAME = 0
    STREAM = 1
    LISTENING = 3
    CUSTOM = 4


class TokenType(Enum):
    USER = 0
    BOT = 1
    EXTERNAL = 2
    APPLICATION = 3
    INTERNAL = 4