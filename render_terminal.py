import os
import re
from PIL import Image, ImageDraw, ImageFont

def render_terminal(
    title: str,
    command_and_output: list[tuple[str, str]], # list of (type, text) where type is 'cmd', 'stdout', 'error', 'success', 'header', 'dim'
    output_path: str,
    width: int = 1000
):
    """
    Renders a realistic macOS terminal window screenshot with exact text and styling.
    """
    # Try finding Menlo or Monaco font
    font_paths = [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Monaco.ttf",
        "/Library/Fonts/Courier New.ttf",
    ]
    font_path = None
    for fp in font_paths:
        if os.path.exists(fp):
            font_path = fp
            break

    font_size = 14
    if font_path:
        try:
            font = ImageFont.truetype(font_path, font_size)
            bold_font = ImageFont.truetype(font_path, font_size)
        except Exception:
            font = ImageFont.load_default()
            bold_font = font
    else:
        font = ImageFont.load_default()
        bold_font = font

    # Calculate required height
    line_height = 20
    header_height = 40
    padding_x = 24
    padding_y = 16

    # Flatten lines to count
    rendered_lines = []
    for item_type, text in command_and_output:
        for line in text.split("\n"):
            rendered_lines.append((item_type, line))

    total_height = header_height + padding_y * 2 + len(rendered_lines) * line_height + 10

    # Create image
    img = Image.new("RGBA", (width, total_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Window background with rounded corners
    bg_color = (24, 24, 32, 255)
    header_color = (36, 36, 48, 255)
    border_color = (60, 60, 75, 255)

    # Draw rounded rectangle for window
    radius = 12
    draw.rounded_rectangle([(0, 0), (width - 1, total_height - 1)], radius=radius, fill=bg_color, outline=border_color, width=1)

    # Draw header
    draw.rounded_rectangle([(0, 0), (width - 1, header_height + radius)], radius=radius, fill=header_color)
    draw.rectangle([(0, header_height), (width - 1, header_height + radius)], fill=header_color)
    draw.line([(0, header_height), (width - 1, header_height)], fill=border_color, width=1)

    # macOS window buttons
    btn_radius = 6
    btn_y = header_height // 2
    buttons = [
        (20, (255, 95, 86)),   # Close red
        (38, (255, 189, 46)),  # Min yellow
        (56, (39, 201, 63)),   # Max green
    ]
    for bx, bcol in buttons:
        draw.ellipse([(bx - btn_radius, btn_y - btn_radius), (bx + btn_radius, btn_y + btn_radius)], fill=bcol)

    # Window Title
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_w) // 2, (header_height - (title_bbox[3] - title_bbox[1])) // 2), title, fill=(180, 180, 195), font=font)

    # Render content lines
    cur_y = header_height + padding_y
    for item_type, line in rendered_lines:
        cur_font = font
        if item_type == "cmd":
            # prompt prefix
            draw.text((padding_x, cur_y), "vaibhav@macbook", fill=(80, 200, 120), font=cur_font)
            p_len = draw.textlength("vaibhav@macbook", font=cur_font)
            draw.text((padding_x + p_len, cur_y), ":", fill=(160, 160, 170), font=cur_font)
            p_len += draw.textlength(":", font=cur_font)
            draw.text((padding_x + p_len, cur_y), "~", fill=(100, 160, 255), font=cur_font)
            p_len += draw.textlength("~", font=cur_font)
            draw.text((padding_x + p_len, cur_y), "$ " + line, fill=(240, 240, 245), font=bold_font)
        elif item_type == "input":
            draw.text((padding_x, cur_y), line, fill=(120, 220, 255), font=cur_font)
        elif item_type == "success":
            draw.text((padding_x, cur_y), line, fill=(100, 230, 140), font=cur_font)
        elif item_type == "error":
            draw.text((padding_x, cur_y), line, fill=(255, 110, 110), font=cur_font)
        elif item_type == "warning":
            draw.text((padding_x, cur_y), line, fill=(255, 200, 80), font=cur_font)
        elif item_type == "header":
            draw.text((padding_x, cur_y), line, fill=(200, 200, 215), font=bold_font)
        elif item_type == "dim":
            draw.text((padding_x, cur_y), line, fill=(120, 120, 135), font=cur_font)
        else: # normal stdout
            draw.text((padding_x, cur_y), line, fill=(215, 215, 225), font=cur_font)
        cur_y += line_height

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Saved: {output_path} ({width}x{total_height})")

if __name__ == "__main__":
    print("Screenshot renderer loaded")
