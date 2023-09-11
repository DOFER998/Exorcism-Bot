from datetime import datetime, timedelta, timezone


def format_dt(dt: datetime) -> str:
    dt = dt.replace(tzinfo=timezone.utc)
    return f'<t:{int(dt.timestamp())}:R>'


def iso_to_time(iso: datetime) -> datetime:
    timestamp = datetime.strptime(iso, "%Y-%m-%dT%H:%M:%S%z").timestamp()
    time = datetime.utcfromtimestamp(timestamp)
    return time
