#!/usr/bin/env python3
"""
Generate hero images via ComfyUI SDXL, save, and inject into .astro pages.
"""
import json, os, requests, time, re, sys, random

COMFY_UI = "http://127.0.0.1:8188"
OUTPUT_DIR = r"C:\HermesPortable\home\scripts\blog-automation\nauru\public\assets\images"
PAGES_DIR = r"C:\HermesPortable\home\scripts\blog-automation\nauru\src\pages"

os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGES = [
    # (slug, astro_subpath, prompt, alt_text)
    ("our-country", ["about", "our-country.astro"], "aerial view of nauru island pacific ocean, tropical island landscape, clear blue water, green palm trees, wide angle", "Aerial view of Nauru Island with turquoise Pacific waters and palm trees"),
    ("history", ["about", "history.astro"], "vintage historical photograph style, old pacific island, nauru phosphate mining, 1900s colonial era", "Historical photograph of phosphate mining operations on Nauru"),
    ("the-people", ["about", "the-people.astro"], "nauru people traditional culture, micronesian community, pacific islanders, warm portrait style, documentary", "Nauruan people in traditional community setting"),
    ("culture", ["about", "culture.astro"], "traditional nauru dance and music, pacific island cultural festival, colorful costumes, outdoor ceremony", "Traditional Nauruan dance performance with colorful costumes"),
    ("economy", ["about", "economy.astro"], "phosphate mining nauru, industrial landscape, mining equipment, pacific island industry, documentary style", "Phosphate mining landscape on Nauru"),
    ("national-days", ["about", "national-days.astro"], "nauru independence day celebration, flag ceremony, official event, pacific island nation pride", "Nauru Independence Day celebration with flag ceremony"),
    ("visa", ["visit", "visa.astro"], "travel documents passport nauru visa, pacific island travel planning, desk with paperwork and map", "Travel documents and passport for Nauru visa planning"),
    ("accommodation", ["visit", "accommodation.astro"], "tropical island hotel resort nauru, beachfront accommodation, pacific paradise, palm trees, sunset", "Beachfront resort accommodation on Nauru at sunset"),
    ("transport", ["visit", "transport.astro"], "nauru international airport, small pacific island airport, airplane on runway, tropical arrival", "Nauru International Airport with airplane on runway"),
    ("weather", ["visit", "weather.astro"], "tropical storm clouds over pacific ocean, nauru weather, dramatic sky, island climate", "Dramatic tropical storm clouds over Pacific Ocean near Nauru"),
    ("currency", ["visit", "currency.astro"], "australian dollars and coins, pacific island currency, money exchange, travel finance", "Australian dollars and coins used as currency in Nauru"),
    ("attire", ["visit", "attire.astro"], "light tropical clothing packing, beach wear, sun hat, nauru travel essentials, casual island style", "Light tropical clothing and beach wear for Nauru travel"),
    ("communications", ["visit", "communications.astro"], "satellite dish communications nauru, pacific island internet, mobile phone tropical setting", "Satellite communications equipment on a Pacific island"),
    ("citizenship", ["services", "citizenship.astro"], "passport and citizenship documents, government building pacific island, official proceedings", "Passport and citizenship documents at a government building"),
    ("health", ["services", "health.astro"], "hospital nauru island, healthcare pacific, medical clinic tropical, modern health facility", "Modern hospital and healthcare facility on Nauru"),
    ("education", ["services", "education.astro"], "school nauru island, children education pacific, classroom tropical, learning and teaching", "School classroom with students on Nauru Island"),
    ("immigration", ["services", "immigration.astro"], "immigration office nauru, customs building airport island, entry documents processing", "Immigration office and customs building on Nauru"),
    ("contact", ["contact", "index.astro"], "nauru government building, administrative office pacific, contact information island style", "Nauru government administrative building"),
    ("about-index", ["about", "index.astro"], "panoramic view nauru island from above, pacific ocean landscape, tropical paradise wide panorama", "Panoramic aerial view of Nauru Island in the Pacific Ocean"),
    ("visit-index", ["visit", "index.astro"], "nauru beautiful beach turquoise water, pacific island paradise, tropical travel destination, sunny day", "Beautiful Nauru beach with turquoise water - tropical paradise"),
    ("services-index", ["services", "index.astro"], "government services nauru, administrative buildings, pacific island infrastructure", "Government service buildings on Nauru"),
]

def queue_prompt(prompt_text, slug):
    """Queue a prompt on ComfyUI and return the prompt_id."""
    prefix = "nauru_" + slug
    seed = random.randint(0, 2**32 - 1)
    workflow = {
        "3": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": 20, "cfg": 7.0, "sampler_name": "euler", "scheduler": "normal", "denoise": 1.0, "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["5", 0]}},
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "sd_xl_base_1.0.safetensors"}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 1200, "height": 800, "batch_size": 1}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt_text, "clip": ["4", 1]}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": "ugly, deformed, text, watermark, blurry, low quality, signature", "clip": ["4", 1]}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
        "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": prefix, "images": ["8", 0]}}
    }
    resp = requests.post(f"{COMFY_UI}/prompt", json={"prompt": workflow})
    resp.raise_for_status()
    data = resp.json()
    prompt_id = data.get("prompt_id")
    print(f"  Queued prompt_id: {prompt_id}")
    return prompt_id, prefix

def poll_history(prompt_id, timeout=300):
    """Poll /history/{prompt_id} until completed. Returns image list."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            resp = requests.get(f"{COMFY_UI}/history/{prompt_id}")
            if resp.status_code == 200:
                data = resp.json()
                if prompt_id in data:
                    prompt_data = data[prompt_id]
                    status = prompt_data.get("status", {})
                    if status.get("completed"):
                        outputs = prompt_data.get("outputs", {})
                        for node_id, node_out in outputs.items():
                            if "images" in node_out:
                                return node_out["images"]
                        return None
                    elif status.get("failed"):
                        print(f"  ERROR: Prompt failed!")
                        return None
        except Exception as e:
            print(f"  Poll error: {e}")
        time.sleep(3)
    print(f"  Timeout waiting for prompt {prompt_id}")
    return None

def download_image(filename, subfolder, slug):
    """Download an image from ComfyUI's output and save with clean name."""
    params = {"filename": filename, "type": "output"}
    if subfolder:
        params["subfolder"] = subfolder
    resp = requests.get(f"{COMFY_UI}/view", params=params, stream=True)
    resp.raise_for_status()
    
    target = os.path.join(OUTPUT_DIR, f"nauru_{slug}_00001_.png")
    with open(target, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"  Saved: {target} ({os.path.getsize(target)//1024} KB)")
    return target

def inject_into_page(slug, astro_subpath, alt_text):
    """Inject hero image into .astro page right after <SubpageLayout opening tag."""
    full_path = os.path.join(PAGES_DIR, *astro_subpath)
    if not os.path.exists(full_path):
        print(f"  WARNING: Page not found: {full_path}")
        return False
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if already injected
    if f"nauru_{slug}_00001_.png" in content:
        print(f"  Already has image injection, skipping.")
        return True
    
    img_tag = f'\n  <img src="/assets/images/nauru_{slug}_00001_.png" alt="{alt_text}" class="hero-image" style="width:100%;border-radius:8px;margin-bottom:2rem">\n'
    
    # Find the <SubpageLayout ... > opening tag and insert after it
    pattern = r'(<SubpageLayout\b[^>]*>\s*\n)'
    match = re.search(pattern, content)
    if match:
        pos = match.end()
        new_content = content[:pos] + img_tag + content[pos:]
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Injected into {os.path.join(*astro_subpath)}")
        return True
    else:
        print(f"  WARNING: No <SubpageLayout> tag found in {full_path}")
        return False

def process_one(slug, astro_subpath, prompt_text, alt_text):
    """Full pipeline for one image."""
    astro_rel = "/".join(astro_subpath)
    print(f"\n{'='*55}")
    print(f"[{slug}] ({astro_rel})")
    sys.stdout.flush()
    
    expected = os.path.join(OUTPUT_DIR, f"nauru_{slug}_00001_.png")
    if os.path.exists(expected):
        print(f"  Image exists ({os.path.getsize(expected)//1024} KB)")
        inject_into_page(slug, astro_subpath, alt_text)
        return True
    
    try:
        prompt_id, prefix = queue_prompt(prompt_text, slug)
    except Exception as e:
        print(f"  FAILED queue: {e}")
        return False
    
    images = poll_history(prompt_id)
    if not images:
        print(f"  FAILED: no output")
        return False
    
    img = images[0]
    filename = img.get("filename")
    subfolder = img.get("subfolder", "")
    print(f"  ComfyUI output: {filename}")
    
    try:
        download_image(filename, subfolder, slug)
    except Exception as e:
        print(f"  FAILED download: {e}")
        return False
    
    inject_into_page(slug, astro_subpath, alt_text)
    return True

def main():
    print(f"Hero image generator: {len(PAGES)} pages")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Pages: {PAGES_DIR}")
    sys.stdout.flush()
    
    success = 0
    failed = []
    
    for slug, astro_subpath, prompt_text, alt_text in PAGES:
        ok = process_one(slug, astro_subpath, prompt_text, alt_text)
        if ok:
            success += 1
        else:
            failed.append(slug)
    
    print(f"\n{'='*55}")
    print(f"Done! {success}/{len(PAGES)} successful.")
    if failed:
        print(f"Failed: {', '.join(failed)}")

if __name__ == "__main__":
    main()
