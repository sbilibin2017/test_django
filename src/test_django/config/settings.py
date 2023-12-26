from split_settings.tools import include

include(
    "components/core.py",
    "components/language.py",
    "components/time.py",
    "components/static.py",
    "components/database.py",
    "components/allowed_hosts.py",
    "components/auth_password_validators.py",
    "components/installed_apps.py",
    "components/templates.py",
    "components/middleware.py",
)
