uasv: str = """
    django.contrib.auth.password_validation.UserAttributeSimilarityValidator
"""

mlv: str = """
    django.contrib.auth.password_validation.MinimumLengthValidator
"""

cpv: str = """
    django.contrib.auth.password_validation.CommonPasswordValidator
"""

npv: str = """
    django.contrib.auth.password_validation.NumericPasswordValidator
"""

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": uasv,
    },
    {
        "NAME": mlv,
    },
    {
        "NAME": cpv,
    },
    {
        "NAME": npv,
    },
]
