import json
import subprocess
from datetime import datetime
from pathlib import Path

import requests


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATUS_FILE = PROJECT_ROOT / "data" / "portfolio_status.json"

PUBLIC_PORTFOLIO_URL = "https://khairulrizal.qzz.io"
PUBLIC_HEALTH_URL = "https://khairulrizal.qzz.io/health"

LOCAL_PORTFOLIO_URL = "http://localhost:5001"
LOCAL_HEALTH_URL = "http://localhost:5001/health"

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

def build_deterministic_summary(status: dict) -> str:
    local_ok = (
        status["local_portfolio"].get("ok") is True
        and status["local_health_endpoint"].get("ok") is True
    )

    docker_ok = status["docker_compose"].get("ok") is True

    if local_ok and docker_ok:
        return (
            "Portfolio is healthy. "
            "The local Flask app, health endpoint, and Docker Compose service are all responding successfully."
        )

    if not local_ok and docker_ok:
        return (
            "Docker Compose appears to be running, but the local Flask app or health endpoint is not responding correctly. "
            "Check the Flask container logs and application startup."
        )

    if not docker_ok:
        return (
            "Docker Compose is not reporting a healthy running state. "
            "Check whether Docker Desktop is running and whether the portfolio container is up."
        )

    return (
        "The portfolio health check found a mixed status. "
        "Review the local app, health endpoint, and Docker Compose details."
    )

def ask_ollama(summary_input: dict) -> str:
    prompt = f"""
You are a local DevOps assistant running on a Windows laptop.

Summarise this portfolio health check in 3 short sentences.
Be clear, practical, and do not exaggerate.

Important:
- Local checks show whether the Flask app is running on the Windows laptop.
- Public checks show whether the Cloudflare Tunnel and public domain are reachable.
- If local checks pass but public checks fail, say the app is running locally but the public route may have a DNS, Cloudflare, or network issue.

Do not include headings.
Do not mention raw JSON.

Health data:
{json.dumps(summary_input, indent=2)}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "Ollama returned no summary.").strip()

    except Exception as error:
        return f"Ollama summary unavailable: {error}"


def main() -> None:
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)

    local_portfolio_check = check_url(LOCAL_PORTFOLIO_URL)
    local_health_check = check_url(LOCAL_HEALTH_URL)

    public_portfolio_check = check_url(PUBLIC_PORTFOLIO_URL)
    public_health_check = check_url(PUBLIC_HEALTH_URL)

    docker_check = check_docker_compose()

    raw_status = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "local_portfolio": local_portfolio_check,
        "local_health_endpoint": local_health_check,
        "public_portfolio": public_portfolio_check,
        "public_health_endpoint": public_health_check,
        "docker_compose": docker_check,
    }

    deterministic_summary = build_deterministic_summary(raw_status)
    ai_summary = ask_ollama(raw_status)

    final_status = {
        **raw_status,
        "status_summary": deterministic_summary,
        "ai_summary": ai_summary,
    }

    STATUS_FILE.write_text(json.dumps(final_status, indent=2), encoding="utf-8")

    print(f"Portfolio health report written to: {STATUS_FILE}")
    print()
    print(ai_summary)


if __name__ == "__main__":
    main()