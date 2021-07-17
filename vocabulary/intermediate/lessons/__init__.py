import os, glob, sys
import importlib.util

parent_dir = os.path.dirname(__file__)
modules = glob.glob1(parent_dir, '*.py')
modules.remove("__init__.py")
lessons_count = len(modules)
import_modules = []

for mdl in modules:
    module_name = mdl.removesuffix(".py")
    module_name = "vocab_inter_" + module_name
    spec = importlib.util.spec_from_file_location(module_name, os.path.join(parent_dir, mdl))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    import_modules.append(getattr(module, module_name))
