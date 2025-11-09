# Open Web-UI Setup

## Prepare Ollama

- [Ollama](https://ollama.com/) made easy to run local LLM directly on your machine.
- Make sure Ollama is installed. Either running on local or container, set `OLLAMA_BASE_URL` in `open-webui.env` so Open Web-Ui can communicate with it.

## Container Setup

- Copy and paste `*.env.example` files to `*.env`
- Run with `docker compose up -d`

## LLM Model Used

- After long trial, I decided to use Qwen3:8B
- Its maximum VRAM that I can run on my own machine
- Using Ollama cloud model is **no help**. There are cache problems (its on cloud, so far i dont find any way to turn off this cache), so directly affecting the `Tools` within Open Web-UI when in development phase
- Even its low on parameter, I can extends the capability of Qwen by using System Prompt and proper variable input and `even_emitter` object.