---
name: generate-montage
description: "Generate a polished screenshot montage or social media collage from supplied images or selected YouTube video frames. Use when asked to create a montage, visual recap, screenshot grid, LinkedIn image, or multi-panel image from a recording."
argument-hint: "Source images or YouTube URL, topics/timestamps, output path, and optional title/date"
---

# Generate Montage

Create a labeled four-panel montage from supplied images or representative frames selected from a video.

## Inputs

- Four topics and short panel labels
- Either four supplied images or a YouTube URL with approximate timestamps
- Output path
- Optional title and subtitle/date

If the user does not specify topics, infer the strongest visually distinct topics from the associated write-up or transcript. Ask only when the source or desired topics are ambiguous.

## Prerequisites

- Python and `uv`
- `yt-dlp` and `ffmpeg` when extracting YouTube frames

Check prerequisites with `command -v`. Before installing missing system packages, tell the user what will be installed and obtain confirmation if the package manager requests it.

## Procedure

1. Identify four visually distinct topics. Prefer demos, product pages, diagrams, code, slides, or recognizable interfaces over four similar talking-head frames.
2. When using a video, download one local copy at no more than 720p:

   ```bash
   yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" \
     --merge-output-format mp4 --no-playlist \
     -o "OUTPUT_DIR/source.%(ext)s" "YOUTUBE_URL"
   ```

3. Capture at least three candidate frames around each topic. Chapter boundaries often show a transition, so include offsets several seconds into the segment:

   ```bash
   ffmpeg -loglevel error -ss SECONDS -i OUTPUT_DIR/source.mp4 \
     -frames:v 1 -q:v 2 OUTPUT_DIR/TOPIC_SECONDS.png -y
   ```

4. Inspect candidates with the image viewer. Select for clear, relevant on-screen content first, then speaker face quality. Reject loading screens, menus, unreadable text, accidental overlays, and duplicate visuals.
5. Compose the four selected images with [compose_montage.py](./compose_montage.py). Each `--panel` value uses `IMAGE::LABEL`:

   ```bash
   uv run .agents/skills/generate-montage/compose_montage.py \
     --output OUTPUT.png \
     --title "PYTHON + AI OFFICE HOURS" \
     --subtitle "SEPTEMBER 1, 2026" \
     --panel "frame1.png::ChatGPT + WebMCP" \
     --panel "frame2.png::VS Code agent hooks" \
     --panel "frame3.png::DSPy.Flex" \
     --panel "frame4.png::LM15"
   ```

6. View the final image and verify:
   - All four panels are relevant and readable.
   - Labels fit without clipping.
   - Tiles meet edge-to-edge without gaps.
   - No text or UI overlaps incoherently.
   - The output is not blank and has the expected dimensions.
7. Remove downloaded video, candidate frames, and contact sheets. Keep only the final montage unless the user asks to retain source assets.

## Composition Rules

- Use exactly four panels in a 2x2 grid.
- Keep labels concise, ideally four words or fewer.
- Preserve screenshots rather than covering them with large captions.
- Use the bundled script's distinct label colors unless the user requests a different palette.
- Do not add a footer or bottom tagline unless explicitly requested.
- Use a header only when it adds useful identity or context.
- Default output is 1200 pixels wide and suitable for LinkedIn and other social feeds.

## Output

Report the final image path and dimensions. Mention any topic for which no clear visual was available.