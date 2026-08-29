> [ERROR] Agent `sceptic` (model `openrouter/z-ai/glm-5.3`) nie odpowiedział: litellm.UnsupportedParamsError: openrouter does not support parameters: ['reasoning_effort'], for model=z-ai/glm-5.3. To drop these, set `litellm.drop_params=True` or for proxy:

`litellm_settings:
 drop_params: true`
. 
 If you want to use these params dynamically send allowed_openai_params=['reasoning_effort'] in your request.