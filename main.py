import logging
import httpx

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()

XENDIT_API_URL = "https://api.xendit.co/v2/invoices"
XENDIT_API_KEY = "xnd_development_rgDDrsF8K3Jf5uOQ3ZKY8Zn4hfbXvmTsws9IgiLAG24Xu3KUZzXXzZ2h6qG23DT"


@app.post("/payment")
async def handle_webhook(request: Request):
    payload = dict(await request.form())

    xendit_payload = {
        "external_id": payload.get("external_id"),
        "amount": payload.get("amount"),
        "payer_email": payload.get("payer_email"),
        "description": payload.get("description"),
        "success_redirect_url": payload.get("success_redirect_url"),
        "failure_redirect_url": payload.get("failure_redirect_url"),
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=XENDIT_API_URL,
            auth=(XENDIT_API_KEY, ''),
            json=xendit_payload,
            headers={"Content-Type": "application/json"}
        )

    if response.status_code != 200:
        logging.error(f"Failed to send data to Xendit: {response.text}")
        raise HTTPException(status_code=response.status_code,
                            detail="Failed to create invoice")

    response_data = response.json()
    redirect = response_data.get("invoice_url")

    return RedirectResponse(url=redirect, status_code=302)

