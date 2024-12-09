from datetime import datetime
import pytz

date_created_str = "2024-01-02 15:43:43"

# Convert date_created to datetime in ISO 8601 format (2024-10-21T10:22:46.996Z)
def convert_to_utc(date_created_str):
    date_created_dt = datetime.strptime(date_created_str, '%Y-%m-%d %H:%M:%S')
    local_tz = pytz.timezone('Asia/Bangkok')
    local_tz_date_created = local_tz.localize(date_created_dt)
    date_created_utc = local_tz_date_created.astimezone(pytz.utc).replace(
        microsecond=0).isoformat().replace('+00:00', ':00.000Z')
    return date_created_utc

def convert_to_utc_prod(date_created_str):
    date_modified_dt = datetime.strptime(date_created_str,'%Y-%m-%d %H:%M:%S')
    local_tz_date_modified = pytz.timezone('Asia/Bangkok')
    local_time_with_tz_date_modified = local_tz_date_modified.localize(date_modified_dt)
    date_modified_utc = local_time_with_tz_date_modified.astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')
    return date_modified_utc

dt = convert_to_utc_prod(date_created_str)
dt_type = type(dt)
print(dt_type)