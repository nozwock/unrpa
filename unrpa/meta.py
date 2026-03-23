import importlib.metadata

_metadata = importlib.metadata.metadata("unrpa")

name = _metadata["Name"]
version = _metadata["Version"]
description = _metadata["Summary"]
