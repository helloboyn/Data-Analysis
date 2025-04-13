```python
import json

def enhance_article(article_text):
    """
    Simulates analyzing article text, extracting key points,
    generating image prompts, and generating image URLs.
    Uses placeholder data instead of actual AI calls.
    """
    print(f"Simulating enhancement for: '{article_text[:60]}...'")

    # --- Simulated AI Service Outputs ---
    key_points_info = [
        {"text": "AI enhances diagnostic accuracy significantly.", "overlay": "15% Higher Accuracy"},
        {"text": "Streamlines workflows, reducing reporting times.", "overlay": "25% Faster Reporting"},
        {"text": "Requires careful validation and clinician trust.", "overlay": None}
    ]
    prompts = [
        "Professional healthcare aesthetic: AI assisting radiologist, blue/white, 1:1.",
        "Abstract data flow, medical motifs, efficiency theme, green/blue, 1:1.",
        "Trust symbol (shield/hands) with technology, clean design, muted blue, 1:1."
    ]
    base_urls = [f"https://placeholder.ai/img{i+1}_base.png" for i in range(3)]
    overlay_urls = [f"https://placeholder.ai/img{i+1}_overlay.png" for i in range(2)]
    # --- End Simulation ---

    enhanced_content = []
    for i, kp_info in enumerate(key_points_info):
        enhanced_content.append({
            "key_point": {"text": kp_info["text"], "overlay_candidate": kp_info["overlay"]},
            "image_prompt": prompts[i],
            "generated_image_url": base_urls[i],
            "generated_image_with_overlay_url": overlay_urls[i] if kp_info["overlay"] and i < len(overlay_urls) else base_urls[i]
        })

    return {"enhanced_content": enhanced_content}
