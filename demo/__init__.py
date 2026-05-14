import importlib
import pkgutil

modules = [
    importlib.import_module(f".{m.name}", package=__name__)
    for m in sorted(pkgutil.iter_modules([__path__[0]]), key=lambda m: m.name)
    if not m.name.startswith("_")
]
