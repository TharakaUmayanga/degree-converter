def convert_to_dms(degrees: float) -> str:
    d = int(degrees)
    minfloat = (degrees - d) * 60
    m = int(minfloat)
    secfloat = (minfloat - m) * 60
    s = round(secfloat, 2)

    result = f"{d}° {m}' {s}\""
    return result


def convert_to_degrees(d, m, s) -> str:
    degrees = d + (m / 60) + (s / 3600)

    result = f"{degrees:.6f}°"

    return result
