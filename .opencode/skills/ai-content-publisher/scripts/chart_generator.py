import json
import os
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "hugo-site", "static", "images", "charts")


def _ensure_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_bar_chart(data, filename, title, xlabel, ylabel, color="#2563eb"):
    _ensure_dir()
    labels = [d["label"] for d in data]
    values = [d["value"] for d in data]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(labels, values, color=color, width=0.6, edgecolor="#1e3a5f", linewidth=0.5)

    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(values) * 0.01,
                str(v), ha="center", va="bottom", fontsize=11, fontweight="bold")

    ax.set_title(title, fontsize=14, fontweight="bold", pad=16)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="x", rotation=30)
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Chart saved: {path}")
    return f"/images/charts/{filename}"


def generate_pie_chart(data, filename, title):
    _ensure_dir()
    labels = [d["label"] for d in data]
    values = [d["value"] for d in data]
    colors = ["#2563eb", "#3b82f6", "#60a5fa", "#93c5fd", "#bfdbfe", "#dbeafe"]

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        values, labels=None, autopct="%1.1f%%", startangle=90,
        colors=colors[:len(values)], pctdistance=0.78,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5}
    )
    for t in autotexts:
        t.set_fontsize(11)
        t.set_fontweight("bold")

    legend_labels = [f"{l}  ({v})" for l, v in zip(labels, values)]
    ax.legend(wedges, legend_labels, title=title, loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)
    ax.set_title(title, fontsize=14, fontweight="bold", pad=16)
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Chart saved: {path}")
    return f"/images/charts/{filename}"


def generate_line_chart(data, filename, title, xlabel, ylabel, color="#2563eb"):
    _ensure_dir()
    labels = [d["label"] for d in data]
    values = [d["value"] for d in data]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(labels, values, marker="o", linewidth=2.5, color=color,
            markerfacecolor=color, markersize=8, markeredgecolor="white", markeredgewidth=1.5)
    ax.fill_between(range(len(labels)), values, alpha=0.1, color=color)

    for i, v in enumerate(values):
        ax.text(i, v + max(values) * 0.02, str(v), ha="center", va="bottom", fontsize=11, fontweight="bold")

    ax.set_title(title, fontsize=14, fontweight="bold", pad=16)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Chart saved: {path}")
    return f"/images/charts/{filename}"


def generate_horizontal_bar_chart(data, filename, title, xlabel, ylabel, color="#2563eb"):
    _ensure_dir()
    labels = [d["label"] for d in data]
    values = [d["value"] for d in data]

    fig, ax = plt.subplots(figsize=(10, max(6, len(labels) * 0.5)))
    bars = ax.barh(labels, values, color=color, height=0.6, edgecolor="#1e3a5f", linewidth=0.5)

    for bar, v in zip(bars, values):
        ax.text(bar.get_width() + max(values) * 0.01, bar.get_y() + bar.get_height() / 2,
                str(v), ha="left", va="center", fontsize=11, fontweight="bold")

    ax.set_title(title, fontsize=14, fontweight="bold", pad=16)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Chart saved: {path}")
    return f"/images/charts/{filename}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python chart_generator.py <json_file>")
        print("JSON schema: {\"type\": \"bar|pie|line|hbar\", \"data\": [{\"label\": \"...\", \"value\": N}], \"title\": \"...\", \"xlabel\": \"...\", \"ylabel\": \"...\", \"filename\": \"...\", \"color\": \"...\"}")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        config = json.load(f)

    chart_type = config.get("type", "bar")
    data = config["data"]
    filename = config.get("filename", "chart.png")
    if not filename.endswith(".png"):
        filename += ".png"
    title = config.get("title", "")
    xlabel = config.get("xlabel", "")
    ylabel = config.get("ylabel", "")
    color = config.get("color", "#2563eb")

    generators = {
        "bar": generate_bar_chart,
        "pie": generate_pie_chart,
        "line": generate_line_chart,
        "hbar": generate_horizontal_bar_chart,
    }

    gen = generators.get(chart_type)
    if not gen:
        print(f"Unknown chart type: {chart_type}. Use: bar, pie, line, hbar")
        sys.exit(1)

    gen(data, filename, title, xlabel, ylabel, color)


if __name__ == "__main__":
    main()
