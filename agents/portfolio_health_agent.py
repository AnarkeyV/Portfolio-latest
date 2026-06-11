import json
import subprocess
from datetime import datetime
from pathlib import Path

import requests


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATUS_FILE = PROJECT_ROOT / "data" / "portfolio_status.json"

PORTFOLIO_URL = "https://khairulrizal.qzz.io"
HEALTH_URL = "https://khairulrizal.qzz.io/health"
OLLAMA_MODEL = "llama3.2:1b"


def check_url(url: str) -> dict:
    try:
        response = requests.get(url, timeout=10)
        return {
            "url": url,
            "status_code": response.status_code,
            "ok": response.ok,
            "response_time_ms": round(response.elapsed.total_seconds() * 1000, 2),
        }
    except requests.RequestException as error:
        return {
            "url": url,
            "status_code": None,
            "ok": False,
            "error": str(error),
        }


def check_docker_compose() -> dict:
    try:
        result = subprocess.run(
            ["docker", "compose", "ps", "--format", "json"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )

        if result.returncode != 0:
            return {
                "ok": False,
                "error": result.stderr.strip() or "docker compose ps failed",
            }

        return {
            "ok": True,
            "raw_output": result.stdout.strip(),
        }

    except Exception as error:
        return {
            "ok": False,
            "error": str(error),
        }


def ask_ollama(summary_input: dict) -> str:
    prompt = f"""
You are a local DevOps assistant running on a Windows laptop.

Summarise this portfolio health check in 3 short sentences.
Be clear, practical, and do not exaggerate.

Health data:
{json.dumps(summary_input, indent=2)}
"""

    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL, prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=90,
        )

        if result.returncode != 0:
            return f"Ollama summary unavailable: {result.stderr.strip()}"

        return result.stdout.strip()

    except Exception as error:
        return f"Ollama summary unavailable: {error}"


def main() -> None:
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)

    portfolio_check = check_url(PORTFOLIO_URL)
    health_check = check_url(HEALTH_URL)
    docker_check = check_docker_compose()

    raw_status = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "portfolio": portfolio_check,
        "health_endpoint": health_check,
        "docker_compose": docker_check,
    }

    ai_summary = ask_ollama(raw_status)

    final_status = {
        **raw_status,
        "ai_summary": ai_summary,
    }

    STATUS_FILE.write_text(json.dumps(final_status, indent=2), encoding="utf-8")

    print(f"Portfolio health report written to: {STATUS_FILE}")
    print()
    print(ai_summary)


if __name__ == "__main__":
    main()