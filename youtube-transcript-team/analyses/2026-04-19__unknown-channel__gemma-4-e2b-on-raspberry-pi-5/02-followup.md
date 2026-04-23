# Follow-up

## 바로 실행할 것
- `Pi 5 + SSD + LM Studio CLI + OpenAI-compatible local API` 네 축으로 환경을 먼저 고정하고, 모델은 가장 작은 등급부터 올립니다.
- `GET /v1/models` 같은 가벼운 호출로 로컬 동작 확인 후, 그다음에 에디터 연결과 실제 태스크 테스트로 넘어갑니다.
- `응답 시간`, `CPU 점유`, `RAM 사용량`, `태스크 품질`을 같은 프롬프트로 기록해 `돌아간다`와 `쓸 만하다`를 구분합니다.

## 같이 보면 좋은 영상
- 다른 소형 모델을 같은 Pi 5 조건에서 비교하는 영상
- LM Studio 대신 더 가벼운 서빙 스택으로 edge device를 다루는 영상
- 로컬망 노출 대신 reverse proxy, 인증, 방화벽까지 포함한 보안 구성 영상

## 다음 비교 후보
- `Gemma 4 E2B vs 다른 2B~4B 모델` 비교 영상
- `Raspberry Pi 5 vs 미니 PC` 로컬 LLM 서빙 비교
- `대화형 사용`과 `비대화형 자동화`를 분리해 평가하는 홈랩 운영 영상

## 메모
- 외부 근거 일부는 확인됨: Google 공식 발표는 Gemma 4 E2B/E4B의 멀티모달, native audio input, 128K context, Apache 2.0을 뒷받침합니다.
- LM Studio 공식 문서는 `lms` CLI, headless `llmster`, OpenAI-compatible local API, 네트워크 서빙 문서를 제공합니다.
- 약한 부분은 성능과 실용성 판단입니다. transcript의 `5~6분` 수치는 참고용 데모 결과이지 일반화된 benchmark로 보긴 어렵습니다.
