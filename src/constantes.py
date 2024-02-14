from enum import Enum


# Priemeiro anexo
class FaixasPrimeiroAnexo(Enum):
    PRIMEIRA = {
        "aliquota": 0.04,
        "deducao": 0,
        "icms": 0.34
    }

    SEGUNDA = {
        "aliquota": 0.073,
        "deducao": 5940,
        "icms": 0.34
    }

    TERCEIRA = {
        "aliquota": 0.095,
        "deducao": 13860,
        "icms": 0.335
    }

    QUARTA = {
        "aliquota": 0.107,
        "deducao": 22500,
        "icms": 0.335
    }

    QUINTA = {
        "aliquota": 0.143,
        "deducao": 87300,
        "icms": 0.335
    }

    SEXTA = {
        "aliquota": 0.19,
        "deducao": 378000,
        "icms": 1
    }


# Terceiro anexo
class FaixasTerceiroAnexo(Enum):
    PRIMEIRA = {
        "aliquota": 0.06,
        "deducao": 0,
        "iss": 0.335
    }

    SEGUNDA = {
        "aliquota": 0.112,
        "deducao": 9360,
        "iss": 0.32
    }

    TERCEIRA = {
        "aliquota": 0.135,
        "deducao": 17640,
        "iss": 0.325
    }

    QUARTA = {
        "aliquota": 0.16,
        "deducao": 35640,
        "iss": 0.325
    }

    QUINTA = {
        "aliquota": 0.21,
        "deducao": 125640,
        "iss": 0.335
    }

    SEXTA = {
        "aliquota": 0.33,
        "deducao": 648000,
        "iss": 0.05
    }


# Quinto anexo
class FaixasQuintoAnexo(Enum):
    PRIMEIRA = {
        "aliquota": 0.155,
        "deducao": 0,
        "iss": 0.14
    }

    SEGUNDA = {
        "aliquota": 0.18,
        "deducao": 4500,
        "iss": 0.17
    }

    TERCEIRA = {
        "aliquota": 0.195,
        "deducao": 9900,
        "iss": 0.19
    }

    QUARTA = {
        "aliquota": 0.205,
        "deducao": 17100,
        "iss": 0.21
    }

    QUINTA = {
        "aliquota": 0.23,
        "deducao": 62100,
        "iss": 0.235
    }

    SEXTA = {
        "aliquota": 0.305,
        "deducao": 540000,
        "iss": 1
    }
