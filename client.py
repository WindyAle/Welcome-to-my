# client.py

from model import ModelManager

# --- 1. 동적 의뢰서 생성 ---

def generate_request(model_manager: ModelManager) -> str:
    """
    ModelManager의 채팅 모델을 사용해
    독특하고 창의적인 고객 의뢰서를 생성합니다.
    """
    print("고객 의뢰서 생성 중...")
    
    # AI에게 '고객' 역할을 부여하는 시스템 프롬프트
    system_prompt = (
        "당신은 인테리어 디자이너를 고용하고 싶어하는 고객입니다. "
        "당신이 원하는 방의 디자인을 1-2 문장으로 설명하세요. "
        "구체적이고 독특한 요구사항을 명확하게 말하세요. (예: '미니멀리스트', '아늑한', '고급스러운', '모던한', '화려한') "
        "방에 꼭 있어야 하는 2-3개의 필수 가구 혹은 색깔도 말하세요. "
        "한국어로 말하세요."
    )
    
    # 간단한 사용자 프롬프트
    user_prompt = "저만을 위한 새롭고 독특한 집을 만들어주세요."
    
    try:
        request_text = model_manager.get_chat_response(system_prompt, user_prompt)
        # LLM이 생성한 텍스트에 포함될 수 있는 따옴표 제거
        request_text = request_text.strip().replace('"', '')
        
        print(f"New Request: {request_text}")
        return request_text
    except Exception as e:
        print(f"Error generating request: {e}")
        return "Default Request: A simple room with a bed and a table."

# --- 2. 상세 피드백 생성 ---

def generate_feedback(model_manager: ModelManager, request: str, design_description: str, score: float) -> str:
    """
    ModelManager의 채팅 모델을 사용해
    점수에 기반한 상세한 고객 피드백을 생성합니다.
    """
    print("📄 고객 피드백 생성 중...")
    
    # AI에게 '평가자' 역할을 부여하는 시스템 프롬프트
    system_prompt = (
        "당신은 디자이너의 작품을 평가하는 고객입니다. "
        "당신이 제공한 요구사항과 함께 그에 따라 디자이너가 작업한 결과물을 받았습니다. "
        "당신은 0-5점의 범위에서 평점을 주었습니다. "
        "당신이 '왜' 평점을 그렇게 주었는지 명확한 방법으로 1-2개의 문장으로 디자이너에게 설명해야 합니다. "
        "평점이 높다면 디자이너를 격려하며 칭찬하고, 평점이 낮다면 비판적이며 직설적으로 말하세요. "
        "한국어로 말하세요."
    )
    
    # LLM에게 모든 컨텍스트를 제공하는 사용자 프롬프트
    user_prompt = (
        f"나의 원래 요구사항: \"{request}\"\n"
        f"디자이너의 결과물: \"{design_description}\"\n"
        f"내 평점: {score:.1f} / 5.0\n\n"
        "이것을 참고하여 고객으로서 디자이너에게 피드백을 작성하세요."
    )
    
    try:
        feedback_text = model_manager.get_chat_response(system_prompt, user_prompt)
        feedback_text = feedback_text.strip().replace('"', '')
        
        print("[ 피드백 ]")
        print(feedback_text)
        return feedback_text
    except Exception as e:
        print(f"Error 'generate_feedback()': {e}")
        return "No comment"