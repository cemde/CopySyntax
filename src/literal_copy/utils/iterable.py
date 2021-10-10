from typing import Any
from collections.abc import Iterable

import six


def _iterable(arg: Any) -> bool:
    return isinstance(arg, Iterable) and not isinstance(arg, six.string_types)
