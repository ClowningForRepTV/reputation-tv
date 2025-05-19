def taylor_rerecords(title: str, album: str, year: int) -> str:
    """

    :type album: str
    """
    if album == "reputation" or album == "Taylor Swift":
        return f"{album} is still being clowned"
    return f'Taylor Swift rerecorded \'{title}\' from album {album} in year {year}.'