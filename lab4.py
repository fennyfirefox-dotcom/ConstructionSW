import re


def read_chunks(file_object, chunk_size: int = 4096):
    while True:
        chunk = file_object.read(chunk_size)
        if not chunk:
            break
        yield chunk


def log_lines(file_object):
    log_pattern = re.compile(r'"\s+(\d{3})\s+(\d+|-)')
    for line in file_object:
        res_bytes = (
            len(line.encode("utf-8")) if isinstance(line, str) else len(line)
        )

        line_str = (
            line
            if isinstance(line, str)
            else line.decode("utf-8", errors="ignore")
        )
        match = log_pattern.search(line_str)
        if match:
            sent = match.group(2)
            bytes_sent = int(sent) if sent.isdigit() else 0
        else:
            bytes_sent = 0
        yield res_bytes, bytes_sent


def calc_log_traffic(file_path):
    total_bytes = 0
    total_bytes_sent = 0

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        # Підраховуємо обидва значення за один прохід
        for rec, sent in log_lines(f):
            total_bytes += rec
            total_bytes_sent += sent

    return total_bytes, total_bytes_sent


if __name__ == "__main__":
    file_name = "2017_05_07_nginx.txt"
    try:
        records, b_sent = calc_log_traffic(file_name)
        print(f"Accepted: {records} bytes")
        print(f"Sent: {b_sent} bytes")
    except FileNotFoundError:
        print(f"File not found: {file_name}")