import html
from typing import List
from pydantic import Field
from urllib.parse import quote_plus
from fastapi.responses import HTMLResponse

class Tools:
    def __init__(self):
        pass

    async def maps_embed_directions_iframe(
        self,
        origin: str,
        destination: str,
        mode: str,
        avoid: List[str] = None,
    ) -> HTMLResponse:

        api_key = ""
        if not api_key:
            return "Google Maps API key missing. Set 'GOOGLE_MAPS_EMBED_API_KEY'"

        m = (mode).lower().strip()
        if m not in {"driving", "walking", "bicycling", "transit"}:
            m = "driving"

        parts = [
            f"key={api_key}",
            f"origin={quote_plus(origin)}",
            f"destination={quote_plus(destination)}",
            f"mode={m}",
        ]

        if avoid:
            va = {"tolls", "highways", "ferries"}
            chosen = [a.strip().lower() for a in avoid if a and a.strip().lower() in va]
            if chosen:
                parts.append(f"avoid={'|'.join(chosen)}")

        src_url = f"https://www.google.com/maps/embed/v1/directions?{'&'.join(parts)}"

        page = f"""<!doctype html>
                <html><head><meta charset="utf-8" /></head>
                <body style="margin:0">
                    <iframe
                        src="{html.escape(src_url)}"
                        style="border:0;width:100%;height:520px"
                        loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade"
                        allowfullscreen>
                    </iframe>
                </body></html>"""

        return HTMLResponse(content=page, headers={"Content-Disposition": "inline"})