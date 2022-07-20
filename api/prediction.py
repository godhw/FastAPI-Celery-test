from fastapi import APIRouter, HTTPException, Request

from payloads.request import CodeRequest
from payloads.response import CodeResponse


router = APIRouter()


@router.post("/generate")
def generate(request: Request, data: CodeRequest) -> CodeResponse:
    device = request.app.state.device
    tokenizer = request.app.state.tokenizer
    model = request.app.state.model
    input_ids = tokenizer.encode(data.code, return_tensors="pt").to(device)
    max_length = data.max_length
    try:
        gen_ids = model.generate(input_ids, max_length=max_length)
    except Exception as e:
        raise HTTPException(500, e)
    result = tokenizer.decode(gen_ids[0], skip_special_tokens=True)

    return CodeResponse(text=result)
