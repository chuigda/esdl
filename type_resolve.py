from __future__ import annotations as __vz4ence
from enum import Enum
from dataclasses import dataclass


from esdl_construct import *


@dataclass
class ResolvedField:
    attribute: list[AttrItem]
    name: str
    ty: ResolvedType
    optional: bool
    repeated: bool


@dataclass
class ResolvedCtor:
    attribute: list[AttrItem]
    name: str
    fields: list[ResolvedField]


@dataclass
class ResolvedType:
    pass


@dataclass
class ResolvedSort(ResolvedType):
    attribute: list[AttrItem]
    name: str
    ctors: list[ResolvedCtor]
    has_fixed: bool
    has_flex: bool


class BuiltinType(ResolvedType, Enum):
    Bool = 1
    Byte = 2
    Int16 = 3
    Int32 = 4
    Int64 = 5
    UInt16 = 6
    UInt32 = 7
    Uint64 = 8
    Float32 = 9
    Float64 = 10
    Char = 11


def resolve_types(unresolved: list[Sort]) -> list[ResolvedSort]:
    unresolved_dict: dict[str, Sort] = dict()

    for item in unresolved:
        unresolved_dict[item.name] = item


