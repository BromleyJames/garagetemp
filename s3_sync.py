import datetime as dt
from pathlib import Path


def generate_s3_filename(local_file: Path) -> str:
    timenow = dt.datetime.now()

    # Append the time now, to make the target file unique, otherwise we risk overwriting an existing file
    hour_string = timenow.strftime("%Y%m%d_%H%M%S")
    s3_filename = local_file.stem + "_uploaded_" + hour_string + ".csv"

    return s3_filename


local_file = Path("./output/20231124_01.csv")
a = generate_s3_filename(local_file)
print(a)
