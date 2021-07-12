import os


def set_django_settings_module():
    build_stage = os.environ.get("BUILD_MODE", "LOCAL")
    if build_stage == "PROD":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.prod")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
