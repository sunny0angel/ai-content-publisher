#!/usr/bin/env python3
"""
Hugo Article Publisher
Usage: python hugo_publish.py --commit --push

Creates Hugo markdown files for published articles,
and optionally commits and pushes to GitHub.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

HUGO_SECTIONS = {
    "AI Tutorials": "tutorials",
    "AI for Business": "business",
    "AI for HR": "hr",
    "AI Industry Analysis": "analysis",
    "AI Productivity": "productivity",
}

def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists() and load_dotenv:
        load_dotenv(env_path)

def get_hugo_path():
    load_env()
    path = os.environ.get("HUGO_PROJECT_PATH")
    if not path:
        path = str(Path(__file__).parent.parent.parent / "hugo-site")
    return Path(path)

def create_article(
    title: str,
    description: str,
    content: str,
    language: str,
    category: str,
    tags: list,
    slug: str,
    image_path: str = None,
    draft: bool = True,
):
    hugo_path = get_hugo_path()
    section = HUGO_SECTIONS.get(category, "tutorials")
    
    # Create directory: content/{lang}/{section}/{slug}/
    article_dir = hugo_path / "content" / language / section / slug
    article_dir.mkdir(parents=True, exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Build frontmatter
    frontmatter = {
        "title": title,
        "date": today,
        "lastmod": today,
        "description": description,
        "tags": tags,
        "categories": [category],
        "draft": draft,
        "slug": slug,
    }
    
    if image_path:
        frontmatter["image"] = f"/images/{Path(image_path).name}"
    
    # Write index.md
    frontmatter_yaml = "---\n"
    for key, value in frontmatter.items():
        if isinstance(value, list):
            frontmatter_yaml += f"{key}:\n"
            for item in value:
                frontmatter_yaml += f"  - \"{item}\"\n"
        elif isinstance(value, bool):
            frontmatter_yaml += f"{key}: {'true' if value else 'false'}\n"
        else:
            frontmatter_yaml += f"{key}: \"{value}\"\n"
    frontmatter_yaml += "---\n\n"
    
    article_content = frontmatter_yaml + content
    
    article_path = article_dir / "index.md"
    article_path.write_text(article_content, encoding="utf-8")
    
    print(f"Created: {article_path}", file=sys.stderr)
    return article_path

def copy_image(source_path: str, slug: str):
    """Copy image to Hugo static/images directory"""
    hugo_path = get_hugo_path()
    image_dir = hugo_path / "static" / "images"
    image_dir.mkdir(parents=True, exist_ok=True)
    
    ext = Path(source_path).suffix if source_path else ".jpg"
    dest = image_dir / f"{slug}{ext}"
    
    if os.path.exists(source_path):
        import shutil
        shutil.copy2(source_path, dest)
        print(f"Image copied to: {dest}", file=sys.stderr)
        return str(dest)
    return None

def git_commit_push(commit_message: str = None):
    """Commit and push to GitHub"""
    hugo_path = get_hugo_path()
    
    if not commit_message:
        today = datetime.now().strftime("%Y-%m-%d")
        commit_message = f"Add new articles - {today}"
    
    try:
        subprocess.run(["git", "add", "."], cwd=str(hugo_path), check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", commit_message], cwd=str(hugo_path), check=True, capture_output=True)
        subprocess.run(["git", "push"], cwd=str(hugo_path), check=True, capture_output=True)
        print("Committed and pushed to GitHub.", file=sys.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e.stderr.decode()}", file=sys.stderr)
        return False

def status():
    """Show working tree status"""
    hugo_path = get_hugo_path()
    try:
        result = subprocess.run(["git", "status"], cwd=str(hugo_path), capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Hugo Article Publisher")
    parser.add_argument("--commit", action="store_true", help="Commit changes")
    parser.add_argument("--push", action="store_true", help="Push to remote")
    parser.add_argument("--message", type=str, help="Commit message")
    parser.add_argument("--status", action="store_true", help="Show git status")
    
    args = parser.parse_args()
    
    if args.status:
        status()
    elif args.commit:
        git_commit_push(args.message)
    elif args.push:
        git_commit_push(args.message)
    else:
        parser.print_help()
