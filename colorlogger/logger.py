import sys
import json
from pathlib import Path
from datetime import datetime, timedelta, timezone
from .error import InvalidLogMethod

COLORS = {
    "INFO": "\033[94m",
    "WARN": "\033[93m",
    "ERROR": "\033[91m",
    "DEBUG": "\033[90m",
    "SUCCESS": "\033[92m",
    "RESET": "\033[0m"
}

class ColorLogger:
    def __init__(self):
        self.output = sys.stdout
        self.valid_levels = ["INFO", "WARN", "ERROR", "DEBUG", "SUCCESS"]

    def __getattr__(self, name):
        raise InvalidLogMethod(name, self.valid_levels)

    def _get_timestamp(self, tz_offset):
        try:
            tz = timezone(timedelta(hours=tz_offset))
            return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def _log(self, level, message, context=None, timestamp=True, colors=True, file=None, timezone=-3):
        if level not in self.valid_levels:
            raise ValueError(f"Nível inválido: {level}")

        ts = self._get_timestamp(timezone) if timestamp else ""
        ctx = f" | {json.dumps(context)}" if context else ""
        line = f"[{level}] {ts} - {message}{ctx}" if ts else f"[{level}] {message}{ctx}"

        color = COLORS[level] if colors else ""
        reset = COLORS["RESET"] if colors else ""
        print(f"{color}{line}{reset}", file=self.output)

        if file:
            path = Path(file)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "a", encoding="utf-8") as f:
                f.write(line + "\n")

    def info(self, msg, context=None, timestamp=True, colors=True, timezone=-3):
        self._log("INFO", msg, context, timestamp, colors, None, timezone)

    def warn(self, msg, context=None, timestamp=True, colors=True, timezone=-3):
        self._log("WARN", msg, context, timestamp, colors, None, timezone)

    def error(self, msg, context=None, timestamp=True, colors=True, timezone=-3):
        self._log("ERROR", msg, context, timestamp, colors, None, timezone)

    def debug(self, msg, context=None, timestamp=True, colors=True, timezone=-3):
        self._log("DEBUG", msg, context, timestamp, colors, None, timezone)

    def success(self, msg, context=None, timestamp=True, colors=True, timezone=-3):
        self._log("SUCCESS", msg, context, timestamp, colors, None, timezone)

    def to_file(self, msg, file, level="INFO", context=None, timestamp=True, colors=False, timezone=-3):
        self._log(level.upper(), msg, context, timestamp, colors, file, timezone)

log = ColorLogger()