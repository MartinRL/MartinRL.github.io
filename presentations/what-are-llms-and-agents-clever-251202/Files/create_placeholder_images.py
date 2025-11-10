from PIL import Image, ImageDraw, ImageFont
import os

# Create directory if it doesn't exist
os.makedirs('.', exist_ok=True)

# Define image specifications
images = [
    ('tokens-visualization.png', 'Tokenization\nVisualization', '#5500FF'),
    ('transformer-architecture.png', 'Transformer\nArchitecture', '#00B6FF'),
    ('parameters-network.png', 'Neural Network\nParameters', '#1E8C7F'),
    ('probability-distribution.png', 'Probability\nDistribution', '#FF922D'),
    ('context-window.png', 'Context Window\nMemory', '#043F9C'),
    ('temperature-effects.png', 'Temperature\nEffects', '#3D424B'),
]

# Create placeholder images
for filename, text, color in images:
    # Create a new image with white background
    img = Image.new('RGB', (600, 400), color='white')
    draw = ImageDraw.Draw(img)

    # Add colored rectangle as background
    draw.rectangle([(50, 50), (550, 350)], fill=color)

    # Try to use a default font, fall back to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    # Add text
    lines = text.split('\n')
    y_offset = 150
    for line in lines:
        # Get text bounding box
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Center text
        x = (600 - text_width) // 2
        draw.text((x, y_offset), line, fill='white', font=font)
        y_offset += text_height + 10

    # Add a subtle border
    draw.rectangle([(50, 50), (550, 350)], outline='#E0E0E0', width=2)

    # Save image
    img.save(filename)
    print(f"Created {filename}")

print("\nAll placeholder images created successfully!")